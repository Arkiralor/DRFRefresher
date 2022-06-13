from storyapp.models import Story
from storyapp.serializers import StorySerializer
from general_utilities.language_utils import LanguageHandlers
from searchapp import logger


class SearchHelper:
    """
    Helper methods to search for stories.
    """

    @classmethod
    def find_similiar(cls, sample_body: str = None):
        """
        Method to find similiar stories based on the passed text.
        """
        qryset = Story.objects.all()
        # qryset = Story.objects.filter(body__icontains=sample_body).order_by('-created_at')
        logger.info(f"Found {len(qryset)} candidates.")
        results = []

        for qry in qryset:
            logger.info(f"Comparing {sample_body} with {qry.title}")
            is_alike = LanguageHandlers.check_if_similiar(
                sample_body, qry.body)
            if is_alike.get('are_alike'):
                sim_dict = {
                    'story': StorySerializer(qry).data,
                    'confidence': is_alike.get('confidence')
                }
                results.append(sim_dict)

        results = sorted(
            results, key=lambda data: data['confidence'], reverse=True)

        return results
