import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from gsa_utilities import get_list_of_experts


package = 'ExpertSearch'


class Expert(messages.Message):
    name = messages.StringField(1)
    mail = messages.StringField(2)
    profileUrl = messages.StringField(3)
    imageUrl = messages.StringField(4)
    expertise = messages.StringField(5)
    expertise_social = messages.StringField(6)

    title = messages.StringField(7)
    manager = messages.StringField(8)
    department = messages.StringField(9)
    country = messages.StringField(10)
    address = messages.StringField(11)

    telephone_work = messages.StringField(12)
    telephone_mobile = messages.StringField(13)

class ExpertCollection(messages.Message):
    experts = messages.MessageField(Expert, 1, repeated=True)
    keyword = messages.StringField(2)
    number_of_experts = messages.IntegerField(3)

@endpoints.api(name='expertsearch', version='v1')
class ExpertSearchApi(remote.Service):
    
    def _create_expert(self, x):
        return Expert(name=x["name"],\
                        mail=x["mail"],\
                        profileUrl=x["profileUrl"],\
                        imageUrl=x["imageUrl"],\
                        expertise=x["expertise"],\
                        expertise_social=x["expertise social"],\
                        manager=x["manager"],\
                        department=x["department"],\
                        country=x["country"],\
                        address=x["address"],\
                        telephone_work=x["telephone work"],\
                        telephone_mobile=x["telephone mobile"])

    ID_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            keyword=messages.StringField(1))

    @endpoints.method(ID_RESOURCE, ExpertCollection,
                      path='experts', http_method='GET',
                      name='experts.listExperts')
    def expert_list(self, request):
        experts = [self._create_expert(x) for x in get_list_of_experts(request.keyword)]
        x=ExpertCollection(experts=experts, keyword=request.keyword, number_of_experts=len(experts))
        return x

APPLICATION = endpoints.api_server([ExpertSearchApi])