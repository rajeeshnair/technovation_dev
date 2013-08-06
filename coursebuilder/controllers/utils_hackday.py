from utils import BaseHandler

class HackDayHandler(BaseHandler):
	"""Handler for Hackday page."""
	def get(self):
		"""Handles GET requests."""
		if not self.personalize_page_and_get_enrolled():
			return

		self.template_value['navbar'] = {'hackday': True}
		self.render('hackday.html')