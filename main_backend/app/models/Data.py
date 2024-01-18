from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from app import db


class Data(db.Model):

    __tablename__ = 'data'
    __table_args__ = {
        'extend_existing': True
    }
    
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    site_ID = db.Column(
        db.String
    )
    Title = db.Column(
        db.String
    )
    Description = db.Column(
        db.String
    )
    Synonyms_are_Russian = db.Column(
        db.String
    )
    The_research_method = db.Column(
        db.String
    )
    Which_biomaterial_can_be_used_for_research = db.Column(
        db.String
    )
    How_to_properly_prepare_for_the_study = db.Column(
        db.String
    )
    General_information_about_the_study = db.Column(
        db.String
    )
    What_is_the_research_used_for = db.Column(
        db.String
    )
    When_is_the_study_scheduled = db.Column(
        db.String
    )
    What_do_the_results_mean = db.Column(
        db.String
    )
    Important_notes = db.Column(
        db.String
    )
    What_can_influence_the_result = db.Column(
        db.String
    )
    It_is_also_recommended = db.Column(
        db.String
    )
    Who_appoints_the_study = db.Column(
        db.String
    )
    Literature = db.Column(
        db.String
    )
    Synonyms_are_English = db.Column(
        db.String
    )
    Units_of_measurement = db.Column(
        db.String
    )
    Interpretation_of_the_results = db.Column(
        db.String
    )
    General_information_about_the_disease = db.Column(
        db.String
    )
    The_name_of_the_gene = db.Column(
        db.String
    )
    Localization_of_a_gene_on_a_chromosome = db.Column(
        db.String
    )
    The_function_of_the_gene = db.Column(
        db.String
    )
    A_genetic_marker = db.Column(
        db.String
    )
    Association_of_the_marker_with_disease_descriptioninterpretatio = db.Column(
        db.String
    )
    Diagnostic_significance = db.Column(
        db.String
    )
    The_study_is_recommended_to_be_carried_out_in_a_complex = db.Column(
        db.String
    )
    How_to_prepare_for_the_study = db.Column(
        db.String
    )
    Interpretation_of_the_research_results = db.Column(
        db.String
    )
    The_genetic_marker_is_included_in_the_study = db.Column(
        db.String
    )
    Interpretation_of_the_results_and_diagnostic_significance = db.Column(
        db.String
    )
    The_study_is_recommended_to_be_carried_out_in_combination_with = db.Column(
        db.String
    )
    The_name_of_the_locus_gene = db.Column(
        db.String
    )


    def __repr__(self):
        return f'{self.site_ID}'