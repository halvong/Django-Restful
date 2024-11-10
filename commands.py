from datetime import datetime
from django.utils import timezone
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from toys.models import Toy
from toys.serializers import ToySerializer

toy_release_date = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
toy1 = Toy(name='Snoopy talking action figure', description='Snoopy speaks five languages', release_date=toy_release_date, toy_category='Action figures', was_included_in_home=False)
toy1.save()

toy2 = Toy(name='Hawaiian Barbie', description='Barbie loves Hawaii', release_date=toy_release_date, toy_category='Dolls', was_included_in_home=True)
toy2.save()

serializer_toy1 = ToySerializer(toy1)
serializer_toy2 = ToySerializer(toy2)

#transform to bytes,pg57
json_renderer = JSONRenderer()
toy1_json = json_renderer.render(serializer_toy1.data)
toy2_json = json_renderer.render(serializer_toy2.data)

toy3 = Toy(name="Clash Royale play set", description="6 figures from Clash Royale", release_date="2017-10-09T12:10:00.776594Z", toy_category="Playset", was_included_in_home=False)
toy3.save()

