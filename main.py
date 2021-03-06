# something something something
#
import webapp2
from google.appengine.api import oauth

app = webapp2.WSGIApplication([
		('/participant', 'participant.Participant'),
		], debug=True)
app.router.add(webapp2.Route(r'/participant/<id:[0-9]+><:/?>', 'participant.Participant'))
app.router.add(webapp2.Route(r'/participant/search', 'participant.ParticipantSearch'))
app.router.add(webapp2.Route(r'/ThemeCamps', 'themecamps.ThemeCamps'))
app.router.add(webapp2.Route(r'/ThemeCamps/<cid:[0-9]+>/participant/<pid:[0-9]+></?>', 'themecamps.CampParticipants'))
