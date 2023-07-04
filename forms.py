from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


# vibe check artist form
class PlaylistForm(FlaskForm):
    artist1 = StringField("Artist 1", validators=[DataRequired()])
    artist2 = StringField("Artist 2", validators=[DataRequired()])
    artist3 = StringField("Artist 3", validators=[DataRequired()])
    artist4 = StringField("Artist 4", validators=[DataRequired()])
    artist5 = StringField("Artist 5", validators=[DataRequired()])
    submit = SubmitField("Check My Vibe!")


# dropdown form for recommendations
class RecommendationForm(FlaskForm):
    dropdown = SelectField('Pick a Genre',
                           choices=[('', '--What You In The Mood For--'),
                                    ('Indie', 'Indie'),
                                    ('Pop', 'Pop'),
                                    ('Country', 'Country'),
                                    ('Hip-Hop', 'Hip-Hop'),
                                    ('Workout', 'Workout'),
                                    ('R&B', 'R&B'),
                                    ('Dance/Electronic', 'Dance/Electronic'),
                                    ('Chill', 'Chill'),
                                    ('Christian & Gospel', 'Christian & Gospel'),
                                    ('Sleep', 'Sleep')
                                    ])
    submit = SubmitField("Give Me Tunes!")
