import play_with_word
import pytest
import codecs


@pytest.mark.parametrize('in_text, out_text',
                         [('Cupcake ipsum dolor sit amet. I love caramels topping soufflé I love',
                           'CuPc!aKe !IpsUm Do!lOr !Sit amEt!. I !LovE cAr!aMel!S tOppIn!g so!UffLé I !lOve!')])
def test_word_play(in_text, out_text):
    """ Test if letters are changer accordingly """
    assert play_with_word.word_play(in_text) == out_text
