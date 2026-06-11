from langchain_core.prompts import PromptTemplate
from langchain_litellm import ChatLiteLLM
from pydantic import BaseModel, Field

from agentic_search.rag_state import GraphState

# Instantiation using from_template (recommended)
prompt = PromptTemplate.from_template(
    """You are the RAG router for a personal digital secretary.
Your job is to decide whether the user's message needs retrieval from local personal context before the main assistant answers.
Available local context sources:
- diary: daily work notes, project progress, bug fixes, decisions, and personal activity logs
- memory: long-term user preferences, facts, and important recurring information
Return needs_rag = true when:
- The user asks about something that happened in the past
- The user asks when something was done, fixed, discussed, or decided
- The user asks about project status, progress, recent work, or "how is my/your/the project doing"
- The user refers to personal history, prior conversations, notes, memories, decisions, or records
- The answer depends on private/local context that is not present in the current message
Return needs_rag = false when:
- The user asks a general knowledge question
- The user asks for code explanation or coding help and the current context is enough
- The user is making small talk that does not require personal history
- The answer can be safely given without looking up local notes
When needs_rag is true:
- Provide a concise search_query optimized for retrieving relevant diary/memory entries.
- Do not simply copy the user message if a clearer search query is possible.
When needs_rag is false:
- Set search_query to null.
User message:
{user_message}
"""
)

user_message = "placeholder"


class RagDecision(BaseModel):
    needs_rag: bool
    confidence: float = Field(ge=0, le=1)
    search_query: str | None
    reason: str


llm = ChatLiteLLM(model="openai/gpt-5-nano")
llm_with_structured_output = llm.with_structured_output(RagDecision)


def needs_rag(state: GraphState) -> bool:
    user_message = state["user_query"]
    raw_response = llm_with_structured_output.invoke(prompt.format(user_message=user_message))
    response = RagDecision.model_validate(raw_response)
    return response.needs_rag
