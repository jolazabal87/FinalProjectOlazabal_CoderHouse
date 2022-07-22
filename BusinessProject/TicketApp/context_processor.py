def total_amount_ticket(request):
    total = 0
    if request.user.is_authenticated:
        if 'ticket' in request.session:
            for key, value in request.session["ticket"].items():
                total = total + float(value["price"])
    return { "total_amount_ticket": total}