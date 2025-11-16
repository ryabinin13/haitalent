import pytest
from unittest.mock import AsyncMock
from app.services.question import QuestionService

@pytest.mark.asyncio
class TestQuestionService:
    
    async def test_get_question_success(self):
        mock_question_repo = AsyncMock()
        mock_answer_repo = AsyncMock()
        mock_question = {"id": 1, "text": "Test question", "created_at": "2023-01-01"}
        mock_question_repo.get_id.return_value = mock_question

        service = QuestionService(
            question_repositore=mock_question_repo, 
            answer_repository=mock_answer_repo
        )

        result = await service.get_question(1)
        
        assert result == mock_question
        mock_question_repo.get_id.assert_called_once_with(id=1)

    async def test_get_question_not_found(self):
        mock_question_repo = AsyncMock()
        mock_answer_repo = AsyncMock()
        mock_question_repo.get_id.return_value = None

        service = QuestionService(
            question_repositore=mock_question_repo, 
            answer_repository=mock_answer_repo
        )
        
        result = await service.get_question(999)
        
        assert result is None
        mock_question_repo.get_id.assert_called_once_with(id=999)

