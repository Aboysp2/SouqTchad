from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Listing, Category
from .forms import ListingForm

def listing_list(request):
    query = request.GET.get('q')
    category_slug = request.GET.get('category')
    
    listings = Listing.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.all()

    if query:
        listings = listings.filter(title__icontains=query)
    if category_slug:
        listings = listings.filter(category__slug=category_slug)

    return render(request, 'listings/listing_list.html', {
        'listings': listings,
        'categories': categories,
    })

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk, is_active=True)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user
            listing.save()
            return redirect('listing_detail', pk=listing.pk)
    else:
        form = ListingForm()

    return render(request, 'listings/create_listing.html', {'form': form})
