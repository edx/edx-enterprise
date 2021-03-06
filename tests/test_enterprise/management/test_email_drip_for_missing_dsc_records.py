# -*- coding: utf-8 -*-
"""
Tests for the django management command `email_drip_for_missing_dsc_records`.
"""
import random
from datetime import timedelta

import mock
from pytest import mark

from django.core.management import call_command
from django.test import TestCase
from django.utils import timezone

from consent.models import DataSharingConsent, ProxyDataSharingConsent
from enterprise.management.commands.email_drip_for_missing_dsc_records import PAST_NUM_DAYS
from test_utils.factories import (
    EnterpriseCourseEnrollmentFactory,
    EnterpriseCustomerFactory,
    EnterpriseCustomerUserFactory,
    UserFactory,
)


@mark.django_db
class EmailDripForMissingDscRecordsCommandTests(TestCase):
    """
    Test command `email_drip_for_missing_dsc_records`.
    """
    command = 'email_drip_for_missing_dsc_records'

    def create_enrollments(self, num_learners, update_date=False):
        """
        Create test users and enrollments in database

        """
        course_ids = [
            'course-v1:edX+DemoX+Demo_Course',
            'course-v1:edX+Python+1T2019',
            'course-v1:edX+React+2T2019',
        ]
        enterprise_customer = EnterpriseCustomerFactory(
            name='Starfleet Academy',
            enable_data_sharing_consent=True,
            enforce_data_sharing_consent='at_enrollment',
        )
        learners = []
        for __ in range(num_learners):
            user = UserFactory.create(is_staff=False, is_active=True)
            learners.append(user)
        learners_data = []
        for learner in learners:
            course_id = random.choice(course_ids)
            learners_data.append(
                {
                    'ENTERPRISE_UUID': enterprise_customer.uuid,
                    'EMAIL': learner.email,
                    'USERNAME': learner.username,
                    'USER_ID': learner.id,
                    'COURSE_ID': course_id
                }
            )
            enterprise_customer_user = EnterpriseCustomerUserFactory(
                user_id=learner.id,
                enterprise_customer=enterprise_customer
            )

            enterprise_course_enrollment = EnterpriseCourseEnrollmentFactory(
                enterprise_customer_user=enterprise_customer_user,
                course_id=course_id,
            )
            if update_date:
                enterprise_course_enrollment.created = timezone.now().date() - timedelta(days=PAST_NUM_DAYS)
                enterprise_course_enrollment.save()

    def setUp(self):
        super().setUp()
        self.create_enrollments(num_learners=3, update_date=False)
        self.create_enrollments(num_learners=3, update_date=True)

    @mock.patch(
        'enterprise.management.commands.email_drip_for_missing_dsc_records.DataSharingConsent.objects.proxied_get'
    )
    @mock.patch('enterprise.management.commands.email_drip_for_missing_dsc_records.utils.track_event')
    @mock.patch('enterprise.management.commands.email_drip_for_missing_dsc_records.Command._get_dsc_url')
    def test_email_drip_for_missing_dsc_records(self, mock_get_dsc_url, mock_event_track, mock_dsc_proxied_get):
        """
        Test that email drip event is fired for missing DSC records.
        """
        mock_get_dsc_url.return_value = 'test_url'
        mock_dsc_proxied_get.return_value = DataSharingConsent()
        call_command(self.command)
        self.assertEqual(mock_event_track.call_count, 0)
        mock_dsc_proxied_get.return_value = ProxyDataSharingConsent()
        call_command(self.command)
        self.assertEqual(mock_event_track.call_count, 3)
