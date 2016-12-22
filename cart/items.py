class Items(object):
    def __init__(self, request):
        if request.session.get('items', False):
            self.items = request.session['items']
        else:
            self.items = []

    def add_item(self, request, item_id):
        if item_id not in self.items:
            self.items.append(item_id)
            request.session['items'] = self.items
