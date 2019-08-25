import spacy
from rasa.nlu.components import Component
import typing
from typing import Any, Optional, Text, Dict

if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata

nlp_model = spacy.load('en_core_web_lg') #Load the tokenizer

class SpellCheckerComponent(Component):
    """Component for Spell Checking"""

    # Defines what attributes the pipeline component will
    # provide when called. The listed attributes
    # should be set by the component on the message object
    # during test and train, e.g.
    # ```message.set("entities", [...])```
    provides = []

    # Which attributes on a message are required by this
    # component. e.g. if requires contains "tokens", than a
    # previous component in the pipeline needs to have "tokens"
    # within the above described `provides` property.
    requires = []

    # Defines the default configuration parameters of a component
    # these values can be overwritten in the pipeline configuration
    # of the model. The component should choose sensible defaults
    # and should be able to create reasonable results with the defaults.
    defaults = {}

    # Defines what language(s) this component can handle.
    # This attribute is designed for instance method: `can_handle_language`.
    # Default value is None which means it can handle all languages.
    # This is an important feature for backwards compatibility of components.
    language_list = ['en']

    def __init__(self, component_config=None):
        super(SpellCheckerComponent, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Train this component.

        This is the components chance to train itself provided
        with the training data. The component can rely on
        any context attribute to be present, that gets created
        by a call to :meth:`components.Component.pipeline_init`
        of ANY component and
        on any context attributes created by a call to
        :meth:`components.Component.train`
        of components previous to this one."""
        pass

    def process(self, message, **kwargs):
        print(message.as_dict())
        print("Before:",message.text)
        text = message.text.lower()
        words = nlp_model(text)
        if imported:           
            suggestions = [word.text if spell_checker.spell(word.text) else spell_checker.suggest(word.text)[0] for word in words]       
            message.text = text.join(suggestions)
        print("Later:",message.text)


    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Persist this component to disk for future loading."""

        pass

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Optional[Text] = None,
        model_metadata: Optional["Metadata"] = None,
        cached_component: Optional["Component"] = None,
        **kwargs: Any
    ) -> "Component":
        """Load this component from file."""

        if cached_component:
            return cached_component
        else:
            return cls(meta)


try:
    from hunspell import HunSpell
    spell_checker = HunSpell('./pyhunspell/dictionaries/en-GB/index.dic','./pyhunspell/dictionaries/en-GB/index.aff') #Load Hunspell Dicionary and Affrims
    encoding = spell_checker.get_dic_encoding() #Gets the dictionary Encoding
    imported = True
except ModuleNotFoundError:
    print("Cannot Import HunSpell")
    imported = False


def add_correct_Words(words = []):
    """
    Adds the grammatically correct words to Hunspell Dictionary
    Arguments:
        words = List of the words
    Returns: None
    """
    if imported:
        for word in words:
            spell_checker.add(word)

def remove_word_from_dict(words = []):
    if imported:
        for word in words:
            spell_checker.remove(word)