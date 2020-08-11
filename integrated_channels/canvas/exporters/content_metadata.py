"""
Content metadata exporter for Canvas
"""

from logging import getLogger

from integrated_channels.integrated_channel.exporters.content_metadata import ContentMetadataExporter

LOGGER = getLogger(__name__)


class CanvasContentMetadataExporter(ContentMetadataExporter):
    """
        Canvas implementation of ContentMetadataExporter.
    """
    DATA_TRANSFORM_MAPPING = {
        'name': 'title',
        'course_code': 'number',
        'start_at': 'start',
        'end_at': 'end',
        'integration_id': 'key',
        'syllabus_body': 'description',
        'default_view': 'default_view',
    }

    LONG_STRING_LIMIT = 2000

    def transform_description(self, content_metadata_item):
        """
        Return the course description and enrollment url as Canvas' syllabus body attribute.
        This will display in the Syllabus tab in Canvas.
        """
        enrollment_url = content_metadata_item.get('enrollment_url', None)
        base_description = "<a href={enrollment_url}>To edX Course Page</a><br />".format(
            enrollment_url=enrollment_url)
        full_description = content_metadata_item.get('full_description') or None
        if full_description and len(full_description + enrollment_url) <= self.LONG_STRING_LIMIT:
            description = "{base_description}{full_description}".format(
                base_description=base_description,
                full_description=full_description
            )
        else:
            short_description = content_metadata_item.get(
                'short_description', content_metadata_item.get('title', '')
            )
            description = "{base_description}{short_description}".format(
                base_description=base_description, short_description=short_description
            )

        return description

    def transform_default_view(self, content_metadata_item):  # pylint: disable=unused-argument
        """
        Sets the Home page view in Canvas. We're using Syllabus.
        """
        return 'syllabus'
