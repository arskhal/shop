class Items(object):
    def __init__(self, request):
        if request.session.get('items', False):
            self.items = request.session['items']
        else:
            self.items = []
        self.alert = 'success'

    def add_item(self, request, item_id):
            try:
                item = {'id': item_id, 'count': 1}
                self.items.append(item)
                request.session['items'] = self.items
            except Exception:
                self.alert = 'error'
            return self.alert

    def delete_item(self, request, item_position):
        try:
            self.items.pop(item_position-1)
            request.session['items'] = self.items
        except Exception:
            self.alert = 'error'
        return self.alert

    def change_count(self, request, item_position, count):
        try:
            item = self.items[item_position-1]
            if count > 0:
                item['count'] = count
            else:
                item['count'] = 1
            self.items[item_position-1] = item
            request.session['items'] = self.items
        except Exception:
            self.alert = 'error'
        return self.alert

