"""FormField model"""
from marshmallow import fields
from marshmallow.validate import Range

from app import DB, MA
from .abstract_model import AbstractModel
from app.models import FieldSchema


class FormField(AbstractModel):
    """FormField class"""

    __tablename__ = "form_fields"
    __table_args__ = (
        DB.UniqueConstraint('form_id', 'position', name='unique_form_position'),
    )

    form_id = DB.Column(DB.Integer, DB.ForeignKey('forms.id'), nullable=False)
    field_id = DB.Column(DB.Integer, DB.ForeignKey('fields.id'), nullable=False)
    question = DB.Column(DB.Text, nullable=False)
    position = DB.Column(DB.Integer, nullable=False)

    def __repr__(self):
        return f'form_id: {self.form_id}; field_id: {self.field_id}'


class FormFieldSchema(MA.Schema):
    """
    FormField schema
    """
    class Meta:
        """
        FormField fields to expose
        """
        fields = ("id", "field_id", "question", "position")

    field_id = fields.Integer(required=True)
    question = fields.Str(required=True)
    position = fields.Integer(required=True, validate=Range(min=0))


class FormFieldResponseSchema(MA.Schema):
    """
    FormField put schema
    """
    class Meta:
        """
        Fields of the put schema
        """
        fields = ("id", "field", "question", "position")

    field = fields.Nested(FieldSchema, required=True)
    question = fields.Str(required=True)
    position = fields.Integer(required=True, validate=Range(min=0))

