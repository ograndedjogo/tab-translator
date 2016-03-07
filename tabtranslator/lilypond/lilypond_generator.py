"""
This file defines the tool that enables lilypond file generation from the given music model
"""

from bottle import template
import lilypond_template

class Li_Generator():
    """
    This class defines the object used to transpose a music sheet modeled in tab-translator specific model to lilypond syntax
    """

    def __init__(sheet, output_type):
        """
        Defines a li_generator
        sheet_type: sheet
        param sheet: the music sheet in tab translator specific model
        output_type: str
        pramar output_type: the rendor wanted for graphical representation. e.g. Tab or Staff 
        """
        self.sheet = sheet
        self.type = output_type

    def write_lilypond_file():
        """
        Write the content generated by "build_lilypond()" to a .ly file, named as the music sheet
        """
        with open(str(self.sheet.name) + ".ly", "w+") as output_file:
            output_file.write(build_lilypond())

    def build_lilypond():
        """
        generate the lilypond string from the generator parameters
        """
        time_signature = self.__extract_time_signature()
        notes = self.__extract_notes()

        if "tab" in self.output_type.lower():
            staff = template(lilypond_template.TAB_TEMPLATE, time_signature=time_signature, notes=notes)
        else:
            clef = self.extract_clef()
            staff = template(lilypond_template.STAFF_TEMPLATE, clef=clef, time_signature=time_signature, notes=notes)

        return template(lilypond_template.SHEET_TEMPLATE, staffs=staff)


    def __extract_time_signature():
        """
        Get the time signature from the modeled sheet.
        TODO : Manage special case where time signature change during the music
        """
        pass

    def __extract_notes():
        """
        Get the notes from the model into a single object. (likely list)
        Notes can be both single tone notes or chords
        """
        pass

    def __extract_clef():
        """
        extract the clef from the model.
        TODO: Include clef notion into the model. It is currently unknown from tab-translator model
        """
        pass

