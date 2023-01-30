from import_export import resources, fields
from website.models import *

class SubsResources(resources.ModelResource):
    class Meta:
        model = Subscription
        exclude = ('id')

class ConsultResource(resources.ModelResource):
    class Meta:
        model = Consult
        exclude = ('id')

class CandidateResource(resources.ModelResource):
    career_tag_id__career_tag_name = fields.Field(attribute="career_tag_id__career_tag_name", column_name="Position")
    candidate_name = fields.Field(attribute="candidate_name", column_name="Candidate")
    whatsapp_number = fields.Field(attribute="whatsapp_number", column_name="Whatsapp")
    datetime = fields.Field(attribute="datetime", column_name="Date time")
    email = fields.Field(attribute="email", column_name="Email")
    class Meta:
        model = Candidate
        fields = ('candidate_name', 'career_tag_id__career_tag_name', 'whatsapp_number',  'email', 'datetime')
        export_order = ('candidate_name', 'career_tag_id__career_tag_name', 'whatsapp_number', 'email', 'datetime')
        exclude = ('id','cv')