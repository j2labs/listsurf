from dictshield.document import Document, diff_id_field
from dictshield.fields import (BaseField,
                               StringField,
                               BooleanField,
                               URLField,
                               EmailField,
                               LongField)
# this might get moved
from dictshield.fields.mongo import ObjectIdField

from brubeck.timekeeping import MillisecondField


###
### Social Models
###

@diff_id_field(ObjectIdField, ['id'])
class UserProfile(Document):
    """A UserProfile is essentially any publicly available info about the user.
    Stored in a document separate from the User itself for security.
    """
    # ownable
    owner = ObjectIdField(required=True)
    username = StringField(max_length=30, required=True)

    # streamable
    created_at = MillisecondField()
    updated_at = MillisecondField()

    # unique fields
    name = StringField(max_length=100)
    location = StringField(max_length=100)
    website = URLField()

    _private_fields = [
        'owner',
    ]

    def __unicode__(self):
        return u'%s' % (self.username)


###
### List Models
###
    
@diff_id_field(ObjectIdField, ['id'])
class ListItem(Document):
    """Bare minimum to have the concept of streamed item.
    """
    # ownable
    owner = ObjectIdField(required=True)
    username = StringField(max_length=30, required=True)

    # streamable
    created_at = MillisecondField()
    updated_at = MillisecondField()

    url = URLField()

    _private_fields = [
        'owner',
    ]

    def __unicode__(self):
        return u'%s' % (self.url)
