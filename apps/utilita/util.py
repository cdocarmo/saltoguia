

def unique_slugify(s, queryset, field, max_size=None):
    from django.template.defaultfilters import slugify
    slug=slugify(s)
    
    # while there are a register with field value equal to slug 
    counter = 0  

    while queryset.filter(**{field: slug}):
        
        counter += 1
        if max_size:
            # crop slug:             
            slug = slug[:(max_size-str(counter).__len__())] 
        
        slug = slug + str(counter)
        
    return slug
                