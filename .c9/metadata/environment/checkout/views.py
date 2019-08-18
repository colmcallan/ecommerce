{"filter":false,"title":"views.py","tooltip":"/checkout/views.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":0,"column":0},"end":{"row":60,"column":0},"action":"remove","lines":["from django.shortcuts import render, get_object_or_404, reverse, redirect","from django.contrib.auth.decorators import login_required","from django.contrib import messages","from .forms import MakePaymentForm, OrderForm","from .models import OrderLineItem","from django.conf import settings","from django.utils import timezone","from products.models import Product","import stripe","# Create your views here.","stripe.api_key = settings.STRIPE_SECRET","","","@login_required()","def checkout(request):","    if request.method == \"POST\":","        order_form = OrderForm(request.POST)","        payment_form = MakePaymentForm(request.POST)","","        if order_form.is_valid() and payment_form.is_valid():","            order = order_form.save(commit=False)","            order.date = timezone.now()","            order.save()","","            cart = request.session.get('cart', {})","            total = 0","            for id, quantity in cart.items():","                product = get_object_or_404(Product, pk=id)","                total += quantity * product.price","                order_line_item = OrderLineItem(","                    order=order,","                    product=product,","                    quantity=quantity","                )","                order_line_item.save()","            ","            try:","                customer = stripe.Charge.create(","                    amount=int(total * 100),","                    currency=\"EUR\",","                    description=request.user.email,","                    card=payment_form.cleaned_data['stripe_id']","                )","            except stripe.error.CardError:","                messages.error(request, \"Your card was declined!\")","            ","            if customer.paid:","                messages.error(request, \"You have successfully paid\")","                request.session['cart'] = {}","                return redirect(reverse('products'))","            else:","                messages.error(request, \"Unable to take payment\")","        else:","            print(payment_form.errors)","            messages.error(request, \"We were unable to take a payment with that card!\")","    else:","        payment_form = MakePaymentForm()","        order_form = OrderForm()","    ","    return render(request, \"checkout.html\", {\"order_form\": order_form, \"payment_form\": payment_form, \"publishable\": settings.STRIPE_PUBLISHABLE})",""],"id":292},{"start":{"row":0,"column":0},"end":{"row":61,"column":19},"action":"insert","lines":["from django.shortcuts import render, get_object_or_404, reverse, redirect","from django.contrib.auth.decorators import login_required","from django.contrib import messages","from .forms import MakePaymentForm, OrderForm","from .models import OrderLineItem","from django.conf import settings","from django.utils import timezone","from products.models import Product","import stripe","","# Create your views here.","stripe.api_key = settings.STRIPE_SECRET","","","@login_required()","def checkout(request):","    if request.method == \"POST\":","        order_form = OrderForm(request.POST)","        payment_form = MakePaymentForm(request.POST)","","        if order_form.is_valid() and payment_form.is_valid():","            order = order_form.save(commit=False)","            order.date = timezone.now()","            order.save()","","            cart = request.session.get('cart', {})","            total = 0","            for id, quantity in cart.items():","                product = get_object_or_404(Product, pk=id)","                total += quantity * product.price","                order_line_item = OrderLineItem(","                    order=order,","                    product=product,","                    quantity=quantity","                )","                order_line_item.save()","            ","            try:","                customer = stripe.Charge.create(","                    amount=int(total * 100),","                    currency=\"EUR\",","                    description=request.user.email,","                    card=payment_form.cleaned_data['stripe_id']","                )","            except stripe.error.CardError:","                messages.error(request, \"Your card was declined!\")","            ","            if customer.paid:","                messages.error(request, \"You have successfully paid\")","                request.session['cart'] = {}","                return redirect(reverse('products'))","            else:","                messages.error(request, \"Unable to take payment\")","        else:","            print(payment_form.errors)","            messages.error(request, \"We were unable to take a payment with that card!\")","    else:","        payment_form = MakePaymentForm()","        order_form = OrderForm()","    ","    return render(request, \"checkout.html\", {\"order_form\": order_form, \"payment_form\": payment_form, \"publishable\": settings.STRIPE_PUBLISHABLE})","© 2019 GitHub, Inc."]}],[{"start":{"row":61,"column":0},"end":{"row":61,"column":19},"action":"remove","lines":["© 2019 GitHub, Inc."],"id":293}],[{"start":{"row":60,"column":145},"end":{"row":61,"column":0},"action":"remove","lines":["",""],"id":294}],[{"start":{"row":0,"column":0},"end":{"row":60,"column":145},"action":"remove","lines":["from django.shortcuts import render, get_object_or_404, reverse, redirect","from django.contrib.auth.decorators import login_required","from django.contrib import messages","from .forms import MakePaymentForm, OrderForm","from .models import OrderLineItem","from django.conf import settings","from django.utils import timezone","from products.models import Product","import stripe","","# Create your views here.","stripe.api_key = settings.STRIPE_SECRET","","","@login_required()","def checkout(request):","    if request.method == \"POST\":","        order_form = OrderForm(request.POST)","        payment_form = MakePaymentForm(request.POST)","","        if order_form.is_valid() and payment_form.is_valid():","            order = order_form.save(commit=False)","            order.date = timezone.now()","            order.save()","","            cart = request.session.get('cart', {})","            total = 0","            for id, quantity in cart.items():","                product = get_object_or_404(Product, pk=id)","                total += quantity * product.price","                order_line_item = OrderLineItem(","                    order=order,","                    product=product,","                    quantity=quantity","                )","                order_line_item.save()","            ","            try:","                customer = stripe.Charge.create(","                    amount=int(total * 100),","                    currency=\"EUR\",","                    description=request.user.email,","                    card=payment_form.cleaned_data['stripe_id']","                )","            except stripe.error.CardError:","                messages.error(request, \"Your card was declined!\")","            ","            if customer.paid:","                messages.error(request, \"You have successfully paid\")","                request.session['cart'] = {}","                return redirect(reverse('products'))","            else:","                messages.error(request, \"Unable to take payment\")","        else:","            print(payment_form.errors)","            messages.error(request, \"We were unable to take a payment with that card!\")","    else:","        payment_form = MakePaymentForm()","        order_form = OrderForm()","    ","    return render(request, \"checkout.html\", {\"order_form\": order_form, \"payment_form\": payment_form, \"publishable\": settings.STRIPE_PUBLISHABLE})"],"id":295},{"start":{"row":0,"column":0},"end":{"row":63,"column":4},"action":"insert","lines":["from django.shortcuts import render, get_object_or_404, reverse, redirect","from django.contrib.auth.decorators import login_required","from django.contrib import messages","from .forms import MakePaymentForm, OrderForm","from .models import OrderLineItem","from django.conf import settings","from django.utils import timezone","from products.models import Product","import stripe","","","# Create your views here.","","stripe.api_key = settings.STRIPE_SECRET","","@login_required()","def checkout(request):","    if request.method==\"POST\":","        order_form = OrderForm(request.POST)","        payment_form = MakePaymentForm(request.POST)","        ","        if order_form.is_valid() and payment_form.is_valid():","            order = order_form.save(commit=False)","            order.date = timezone.now()","            order.save()","            ","            cart = request.session.get('cart', {})","            total = 0","            for id, quantity in cart.items():","                product = get_object_or_404(Product, pk=id)","                total += quantity * product.price","                order_line_item = OrderLineItem(","                    order = order, ","                    product = product, ","                    quantity = quantity","                    )","                order_line_item.save()","                ","            try:","                customer = stripe.Charge.create(","                    amount = int(total * 100),","                    currency = \"EUR\",","                    description = request.user.email,","                    card = payment_form.cleaned_data['stripe_id'],","                )","            except stripe.error.CardError:","                messages.error(request, \"Your card was declined!\")","                ","            if customer.paid:","                messages.error(request, \"You have successfully paid\")","                request.session['cart'] = {}","                return redirect(reverse('products'))","            else:","                messages.error(request, \"Unable to take payment\")","        else:","            print(payment_form.errors)","            messages.error(request, \"We were unable to take a payment with that card!\")","    else:","        payment_form = MakePaymentForm()","        order_form = OrderForm()","        ","    return render(request, \"checkout.html\", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})","                ","    "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":63,"column":4},"end":{"row":63,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1566041313557,"hash":"6b41faddb2ea6bfe11ce18307d9a137981f69110"}