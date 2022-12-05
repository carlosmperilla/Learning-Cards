from mainapp.threading_requests_parse_utils import buil_url, get_img_google
from .forms import ValidateForeignWord

from .abstract_views import CardJsonHandling

# Create your views here.
class ShowNativeWord(CardJsonHandling):
    """
        Returns the native word associated with the foreign word.
    """
    
    def actions(self, request, *args, **kwargs):
        super().actions(request, *args, **kwargs)

        self.json_data.update({
            'native_word' : self.card.native_word,
        })


class ReplaceImg(CardJsonHandling):
    """
        Returns a new random image url for the card.
    """

    def actions(self, request, *args, **kwargs):
        super().actions(request, *args, **kwargs)

        url_img = buil_url(self.card, 'foreign_word')
        get_img_google(self.card, url_img)

        self.json_data.update({
            'url_img' : self.card.img,
        })

class CheckAnswer(CardJsonHandling):
    """
        Check if the native word entered corresponds to the foreign word on the card.
        Write down the mistakes and successes.
        Update learning progress by card and by kit.
    """
    
    def actions(self, request, *args, **kwargs):
        super().actions(request, *args, **kwargs)
      
        self.json_data.update({
                'passed' : False,
            })
        
        form = ValidateForeignWord({'native_word': self.data['native_word']})
        if form.is_valid():
            self.json_data['passed'] = self.data["native_word"].lower().split() == self.card.native_word.lower().split()
        
        if self.json_data['passed']:
            self.card.hits += 1
            self.json_data['hits'] = self.card.hits
        else:
            self.card.mistakes += 1
            self.json_data['mistakes'] = self.card.mistakes
        
        self.card.put_success()
        self.kit_by_name.put_successful()
        self.json_data['progress'] = self.kit_by_name.successful