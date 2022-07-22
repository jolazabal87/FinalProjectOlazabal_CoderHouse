class Ticket:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        ticket = self.session.get("ticket")
        if not ticket:
            ticket = self.session["ticket"] = {}
        self.ticket = ticket
            
    def add_ticket(self, movie):
        if(str(movie.id) not in self.ticket.keys()):
            self.ticket[movie.id] = {                
                "movie_id": movie.id,
                "title": movie.title,
                "price": str(movie.price),
                "quantity": 1,
                "img": movie.img.url                                    
            }
        else:
            for key, value in self.ticket.items():
                if key == str(movie.id):
                    value["quantity"] = value["quantity"] + 1
                    value["price"] = float(value["price"]) + movie.price
                    break
        self.save_ticket()
        
    def save_ticket(self):
        self.session["ticket"] = self.ticket
        self.session.modified = True
        
    def delete_ticket(self, movie):
        movie.id = str(movie.id)
        if movie.id in self.ticket:
            del self.ticket[movie.id]
            self.save_ticket()
            
    def subtract_ticket(self, movie):
        for key, value in self.ticket.items():
            if key == str(movie.id):
                value["quantity"] = value["quantity"] - 1
                value["price"] = float(value["price"]) - movie.price
                if value["quantity"] < 1:
                    self.delete_ticket(movie)
                break
        self.save_ticket()
    
    def clean_ticket(self):
        self.session["ticket"] = {}
        self.session.modified = True