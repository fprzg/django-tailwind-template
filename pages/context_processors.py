from django.urls import reverse

def common_context(request):
    ctx =  {
        'pages': {
            'Home': reverse('index'),
            'About Us': reverse('about'),
            #'Testimonials': reverse('testimonials'),
            #'Our Work': reverse('our-work'),
            #'News': reverse('news'),
            #'Contact': reverse('contact'),
        },
        'hero': {
            'title': 'Let you home be unique',
            'paragraph': 'There are many variations of the passages of lorem Ipsum from available,variations of the passages.',
            'button': 'Get free estimation',
        },
        'steps': [
            {
                'icon': 'ri-compasses-2-line',
                'title': 'Project Planning',
                'paragraph': 'There are many variations of the passages of lorem Ipsum from available,variations of the passages.'
            },
            {
                'icon': 'ri-magic-line',
                'title': 'Gaining Materials',
                'paragraph': 'There are many variations of the passages of lorem Ipsum from available,variations of the passages.'
            },
            {
                'icon': 'ri-tools-line',
                'title': 'Gaining Materials',
                'paragraph': 'There are many variations of the passages of lorem Ipsum from available,variations of the passages.'
            }
        ],
        'about': {
            'text_title': 'We Create The Art Of Stylish Living Stylishly',
            'text_paragraph': 'It is a long established fact that a reader will be distracted by the of readable content of a page when lookings at its layouts the points of using that it has a more-or-less normal.',
            'phone_number': '(+1) 884 234 2343',
            'phone_paragraph': 'Call Us Anytime',
        },
        'testimonials': [
            {
                'img': '/static/img/testimonial/01.png',
                'name': 'Nattasha Mith',
                'location': 'Greenville, USA',
                'paragraph': 'Lorem Ipsum is simply dummy text of the typesetting industry. Ipsum has been.',
            },
            {
                'img': '/static/img/testimonial/02.png',
                'name': 'Nattasha Mith',
                'location': 'Greenville, USA',
                'paragraph': 'Lorem Ipsum is simply dummy text of the typesetting industry. Ipsum has been.',
            },
            {
                'img': '/static/img/testimonial/03.png',
                'name': 'Nattasha Mith',
                'location': 'Greenville, USA',
                'paragraph': 'Lorem Ipsum is simply dummy text of the typesetting industry. Ipsum has been.',
            },
        ],
        'brands': [
            '/static/img/brands/01.svg',
            '/static/img/brands/02.svg',
            '/static/img/brands/03.svg',
            '/static/img/brands/04.svg',
            '/static/img/brands/05.svg',
        ],
        'projects': {
            'text': {
                'title': 'Follow Our Projects',
                'paragraph': 'It is a long established fact that a reader will be distracted by the of readable content of page lookings at its layouts points.',
            },
            'list': [
                {
                    'name': 'Modern Kitchen',
                    'desc': 'Decor/Architecture',
                    'img': '/static/img/work/01.png',
                },
                {
                    'name': 'Modern Kitchen',
                    'desc': 'Decor/Architecture',
                    'img': '/static/img/work/02.png',
                },
                {
                    'name': 'Modern Kitchen',
                    'desc': 'Decor/Architecture',
                    'img': '/static/img/work/03.png',
                },
                {
                    'name': 'Modern Kitchen',
                    'desc': 'Decor/Architecture',
                    'img': '/static/img/work/04.png',
                },
            ],
        },
        'stats': {
            'Years Of Experience': '12',
            'Projects Completed': '85',
            'Active Projects': '15',
            'Happy Customers': '95',
        },
        'news': [
            {
                'img': '/static/img/news/01.png',
                'title': 'Let\'s Get Solution For Building Construction Work',
                'date': '22 June, 2024',
            },
            {
                'img': '/static/img/news/02.png',
                'title': 'Let\'s Get Solution For Building Construction Work',
                'date': '22 June, 2024',
            },
            {
                'img': '/static/img/news/03.png',
                'title': 'Let\'s Get Solution For Building Construction Work',
                'date': '22 June, 2024',
            },
        ],
        'contact': {
            'cta': 'Do you want to join Interno?',
            'desc': 'It is a long established fact that a reader will be distracted lookings.',
            'button': 'Connect with us',
        },
        'services': {
            'Kitchen': '#',
            'Living Area': '#',
            'Bathroom': '#',
            'Bedroom': '#',
        },
        'socials': {
            'facebook': 'https://facebook.com',
            'twitter': 'https://twitter.com',
            'instagram': 'https://instagram.com',
        },
        'year': {
            '2025',
        }
    }

    return ctx