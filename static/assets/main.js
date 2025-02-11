  // mobile menu list
  const menuModules = {
    menuList: [{
            name: 'Home',
            isOpen: false,
            subMenus: [{
                    name: 'Home 1',
                    href: 'index-1.html'
                },
                {
                    name: 'Home 2',
                    href: 'index-2.html'
                },
                {
                    name: 'Home 3',
                    href: 'index-3.html'
                },
            ]
        },
        {
            name: 'Shop',
            isOpen: false,
            subMenus: [{
                    name: 'List view',
                    href: 'list-view.html'
                },
                {
                    name: 'Grid view',
                    href: 'grid-view.html'
                },
                {
                    name: 'Grid view 2',
                    href: 'grid-view-2.html'
                },
                {
                    name: 'Shopping Cart',
                    href: 'shopping-cart.html'
                },
                {
                    name: 'Product view',
                    href: 'product-view.html'
                },
            ]
        },
        {
            name: 'My Account',
            isOpen: false,
            subMenus: [{
                    name: 'My Account',
                    href: 'my-account.html'
                },
                {
                    name: 'Login',
                    href: 'login.html'
                },
                {
                    name: 'Register',
                    href: 'register.html'
                },
                {
                    name: 'Forgot Password',
                    href: 'forgot-password.html'
                },
            ]
        },
        {
            name: 'Other Pages',
            isOpen: false,
            subMenus: [{
                    name: 'About Us',
                    href: 'about.html'
                },
                {
                    name: 'Contact Us',
                    href: 'contact.html'
                },
                {
                    name: 'Track Order',
                    href: 'track-order.html'
                },
                {
                    name: 'FAQ',
                    href: 'faq.html'
                },
                {
                    name: '404',
                    href: '404.html'
                },
                {
                    name: 'Checkout',
                    href: 'checkout.html'
                },
                {
                    name: 'Payment',
                    href: 'payment.html'
                },
                {
                    name: 'Order Complete',
                    href: 'order-complete.html'
                },
            ]
        },
    ],
    toggleMenu(index) {
        if (this.menuList[index].isOpen) {
            this.menuList[index].isOpen = false
        } else {
            this.menuList.forEach(menu => menu.isOpen = false)
            this.menuList[index].isOpen = true
        }
    }
}

// category list
const categoryModules = {
    categoryList: [{
            icon: `<svg width="20" height="20" viewBox="0 0 32 32">
                        <path fill="currentColor"
                            d="M10 3C7.805 3 6.203 4.605 5.281 6.5C4.36 8.395 3.961 10.68 4 12.688c.047 2.332 1.063 4.687 1.063 4.687l.28.625h8.407l.219-.75s.789-2.941 1-5.75c.082-1.105.047-3.027-.563-4.844c-.304-.91-.746-1.8-1.469-2.5C12.216 3.457 11.188 3 10 3zm12 0c-1.188 0-2.215.457-2.938 1.156c-.722.7-1.164 1.59-1.468 2.5c-.61 1.817-.645 3.739-.563 4.844c.211 2.809 1 5.75 1 5.75l.219.75h8.406l.282-.625S27.953 15.02 28 12.687c.04-2.007-.36-4.292-1.281-6.187C25.797 4.605 24.195 3 22 3zM10 5c.703 0 1.129.203 1.531.594c.403.39.762 1.011 1 1.718c.473 1.415.531 3.215.469 4.063c-.164 2.176-.684 3.996-.844 4.625H6.72c-.242-.684-.692-2.016-.719-3.344c-.035-1.695.355-3.761 1.094-5.281C7.832 5.855 8.77 5 10 5zm12 0c1.23 0 2.168.855 2.906 2.375c.739 1.52 1.125 3.586 1.094 5.281c-.027 1.328-.477 2.66-.719 3.344h-5.437c-.16-.629-.68-2.45-.844-4.625c-.063-.848-.004-2.648.469-4.063c.238-.707.597-1.328 1-1.718C20.87 5.204 21.297 5 22 5zM5 21v1c-.012 1.379.121 2.988.813 4.406C6.502 27.824 7.957 29 10 29c2.262 0 3.98-2.215 4-5c.004-.645-.023-1.402-.25-2.25l-.188-.75zm13.438 0l-.188.75c-.227.848-.254 1.605-.25 2.25c.02 2.785 1.738 5 4 5c2.043 0 3.496-1.176 4.188-2.594c.69-1.418.824-3.027.812-4.406v-1zM7.155 23h4.75c.035.328.098.664.094 1c-.016 2.023-1.07 3-2 3c-1.379 0-1.95-.535-2.406-1.469c-.328-.668-.367-1.629-.438-2.531zm12.938 0h4.75c-.07.902-.11 1.863-.438 2.531C23.95 26.465 23.38 27 22 27c-.93 0-1.984-.977-2-3c-.004-.336.059-.672.094-1z" />
                    </svg>`,
            name: 'Shoes',
            href: '#',
        },
        {
            icon: `<svg width="20" height="20" viewBox="0 0 32 32">
                        <path fill="currentColor"
                            d="M16 2c-2.2 0-4 1.8-4 4a3.96 3.96 0 0 0 1.125 2.75C11.273 9.773 10 11.746 10 14v5.406l.281.313L12 21.437V30h2v-9.406l-.281-.313L12 18.563V14c0-2.219 1.781-4 4-4c2.219 0 4 1.781 4 4v4.563l-1.719 1.718l-.281.313V30h2v-8.563l1.719-1.718l.281-.313V14c0-2.254-1.273-4.227-3.125-5.25A3.958 3.958 0 0 0 20 6c0-2.2-1.8-4-4-4zm0 2c1.117 0 2 .883 2 2s-.883 2-2 2s-2-.883-2-2s.883-2 2-2z" />
                    </svg>`,
            name: 'Men',
            isOpen: false,
            subCategories: [{
                    name: 'Hot Sale',
                    isOpen: false,
                    megaCategories: [{
                            name: 'Hoodies $ Sweatshirts',
                            href: '#'
                        },
                        {
                            name: 'T-Shirt',
                            href: '#'
                        },
                        {
                            name: "Men's Sets",
                            href: '#'
                        },
                        {
                            name: 'Jacket',
                            href: '#'
                        },
                        {
                            name: 'Shoes',
                            href: '#'
                        },
                    ]
                },
                {
                    name: 'Bottoms',
                    isOpen: false,
                    megaCategories: [{
                            name: 'Casual Pants',
                            href: '#'
                        },
                        {
                            name: "Men's Sleep & Lounge",
                            href: '#'
                        },
                        {
                            name: 'Jeans',
                            href: '#'
                        },
                        {
                            name: 'Shorts',
                            href: '#'
                        },
                        {
                            name: 'Towel',
                            href: '#'
                        },
                    ]
                },
                {
                    name: 'Outerwear & Jackets',
                    isOpen: false,
                    megaCategories: [{
                            name: 'Jacket',
                            href: '#'
                        },
                        {
                            name: 'Sweaters',
                            href: '#'
                        },
                        {
                            name: 'Casual Faux Leather',
                            href: '#'
                        },
                        {
                            name: 'Parks',
                            href: '#'
                        },
                        {
                            name: 'Jeans',
                            href: '#'
                        },
                    ]
                },
                {
                    name: 'Underwear & Loun',
                    isOpen: false,
                    megaCategories: [{
                            name: 'Boxes',
                            href: '#'
                        },
                        {
                            name: 'Berifs',
                            href: '#'
                        },
                        {
                            name: 'Long Johns',
                            href: '#'
                        },
                        {
                            name: "Men's Sleep & Lounge",
                            href: '#'
                        },
                        {
                            name: 'Parks',
                            href: '#'
                        },
                    ]
                },
                {
                    name: 'Accessories',
                    isOpen: false,
                    megaCategories: [{
                            name: 'Scarves',
                            href: '#'
                        },
                        {
                            name: 'Skullies & Beanies',
                            href: '#'
                        },
                        {
                            name: 'Casual Faux Leather',
                            href: '#'
                        },
                        {
                            name: 'Prescription Glasses',
                            href: '#'
                        },
                        {
                            name: 'Belt',
                            href: '#'
                        },
                    ]
                },
                {
                    name: 'Novelty & Special',
                    isOpen: false,
                    megaCategories: [{
                            name: 'Cosplay Costumes',
                            href: '#'
                        },
                        {
                            name: 'Stage & Dance Wear',
                            href: '#'
                        },
                        {
                            name: 'Exotic Apparel',
                            href: '#'
                        },
                        {
                            name: 'Scarves',
                            href: '#'
                        },
                        {
                            name: "Men's Sets",
                            href: '#'
                        },
                    ]
                },
            ]
        },
        {
            icon:`<svg width="20" height="20" viewBox="0 0 32 32">
                        <path fill="currentColor"
                            d="M16 2c-2.2 0-4 1.8-4 4c0 1.129.488 2.145 1.25 2.875a4.531 4.531 0 0 0-.656.563c-.84.89-1.364 2.078-1.594 3.374h.031l-2 10L8.781 24H13v6h2v-6h2v6h2v-6h4.219l-.25-1.188l-2-10c-.23-1.234-.73-2.41-1.563-3.312a4.752 4.752 0 0 0-.687-.625C19.492 8.145 20 7.137 20 6c0-2.2-1.8-4-4-4zm0 2c1.117 0 2 .883 2 2s-.883 2-2 2s-2-.883-2-2s.883-2 2-2zm0 6c.828 0 1.422.316 1.938.875c.515.559.921 1.387 1.093 2.313L20.781 22H11.22l1.75-8.813H13c.176-1 .559-1.84 1.063-2.374c.503-.536 1.09-.813 1.937-.813z" />
                    </svg>`,
            name: 'Women',
        },
        {
            icon:`<svg width="20" height="20" viewBox="0 0 256 256">
                        <path fill="currentColor"
                            d="M237.7 66.3a8.1 8.1 0 0 0-11.4 0L192 100.7L155.3 64l34.4-34.3a8.1 8.1 0 0 0-11.4-11.4L144 52.7l-26.3-26.4a8.1 8.1 0 0 0-11.4 11.4l6.4 6.3L61 95.7a40.1 40.1 0 0 0 0 56.6L76.7 168l-50.4 50.3a8.1 8.1 0 0 0 0 11.4a8.2 8.2 0 0 0 11.4 0L88 179.3l15.7 15.7a40.1 40.1 0 0 0 56.6 0l51.7-51.7l6.3 6.4a8.2 8.2 0 0 0 11.4 0a8.1 8.1 0 0 0 0-11.4L203.3 112l34.4-34.3a8.1 8.1 0 0 0 0-11.4ZM149 183.7a24 24 0 0 1-34 0L72.3 141a24.1 24.1 0 0 1 0-34L124 55.3l76.7 76.7Z" />
                    </svg>`,
            name: 'Electronisc',
        },
        {
            icon:`<svg width="20" height="20" viewBox="0 0 28 28">
                        <path fill="currentColor"
                            d="M22 26h-3a1 1 0 0 1-.993-.883L18 25v-8a1 1 0 0 1 .883-.993L19 16h5.5v-2c0-5.799-4.701-10.5-10.5-10.5S3.5 8.201 3.5 14v2H9a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H6a4 4 0 0 1-4-4v-8C2 7.373 7.373 2 14 2s12 5.373 12 12v8a4 4 0 0 1-3.8 3.995L22 26h-3h3ZM8.5 17.5h-5V22A2.5 2.5 0 0 0 6 24.5h2.5v-7Zm16 0h-5v7H22a2.5 2.5 0 0 0 2.5-2.5v-4.5Z" />
                    </svg>`,
            name: 'Headphones',
        },
        {
            icon:`<svg width="20" height="20" viewBox="0 0 48 48">
                        <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                            stroke-width="4">
                            <path d="M34.956 31L31 44H17l-3.957-13m0-14L17 4h14l3.956 13" />
                            <path
                                d="M37 24c0 2.577-.75 4.98-2.044 7A12.99 12.99 0 0 1 24 37a12.99 12.99 0 0 1-10.956-6A12.94 12.94 0 0 1 11 24c0-2.577.75-4.98 2.044-7A12.99 12.99 0 0 1 24 11a12.99 12.99 0 0 1 10.956 6A12.94 12.94 0 0 1 37 24Z" />
                            <path d="M24 17v7l4 4" />
                        </g>
                    </svg>`,
            name: 'Watches',
        },
        {
            icon:`<svg width="20" height="20" viewBox="0 0 1024 1024">
                        <path fill="currentColor"
                            d="M960 95.808H64c-35.184 0-64 28.8-64 64V704c0 35.184 28.816 63.983 64 63.983h416v96.208H320c-17.664 0-32 14.336-32 32s14.336 32 32 32h384c17.664 0 32-14.336 32-32s-14.336-32-32-32H544v-96.208h416c35.184 0 64-28.8 64-63.983V159.808c0-35.2-28.816-64-64-64zM960 704H64V159.808h896V704z" />
                    </svg>`,
            name: 'Computer',
            isOpen: false,
            subCategories: [{
                    name: 'Macbook',
                    isOpen: false,
                    megaCategories: [{
                            name: 'Macbook m1',
                            href: '#'
                        },
                        {
                            name: 'Macbook pro',
                            href: '#'
                        },
                        {
                            name: 'Macbook air',
                            href: '#'
                        },
                        {
                            name: 'macbook 2015',
                            href: '#'
                        },
                        {
                            name: 'macbook 2020',
                            href: '#'
                        },
                    ]
                },
                {
                    name: 'Laptop',
                    isOpen: false,
                    megaCategories: [{
                            name: 'Razer',
                            href: '#'
                        },
                        {
                            name: 'Hp Laptop',
                            href: '#'
                        },
                        {
                            name: 'Dell Notebook',
                            href: '#'
                        },
                        {
                            name: 'Asus',
                            href: '#'
                        },
                        {
                            name: 'Lenovo',
                            href: '#'
                        },
                    ]
                },
                {
                    name: 'Dasktop',
                    isOpen: false,
                    megaCategories: [{
                            name: 'Brand Dasktop',
                            href: '#'
                        },
                        {
                            name: 'All in one pc',
                            href: '#'
                        },
                        {
                            name: 'Mini PC',
                            href: '#'
                        },
                        {
                            name: 'Customize PC',
                            href: '#'
                        },
                        {
                            name: 'Dasktop Accessories',
                            href: '#'
                        },
                    ]
                },
                {
                    name: 'Monitor',
                    isOpen: false,
                    megaCategories: [{
                            name: 'Samsung',
                            href: '#'
                        },
                        {
                            name: 'Philips',
                            href: '#'
                        },
                        {
                            name: 'LG',
                            href: '#'
                        },
                        {
                            name: 'HP',
                            href: '#'
                        },
                        {
                            name: 'Xiaomi',
                            href: '#'
                        },
                    ]
                },
                {
                    name: 'Accessories',
                    isOpen: false,
                    megaCategories: [{
                            name: 'Dasktop Ram',
                            href: '#'
                        },
                        {
                            name: 'Motherboard',
                            href: '#'
                        },
                        {
                            name: 'SSD Card',
                            href: '#'
                        },
                        {
                            name: 'Hard disk',
                            href: '#'
                        },
                        {
                            name: 'Processor',
                            href: '#'
                        },
                    ]
                },
                {
                    name: 'Gaming',
                    isOpen: false,
                    megaCategories: [{
                            name: 'Gaming console',
                            href: '#'
                        },
                        {
                            name: 'Gaming Chair',
                            href: '#'
                        },
                        {
                            name: 'Gaming Desk',
                            href: '#'
                        },
                        {
                            name: 'Gaming Controller',
                            href: '#'
                        },
                        {
                            name: 'Keyboard',
                            href: '#'
                        },
                    ]
                }
            ]
        },
        {
            icon:`<svg width="20" height="20" viewBox="0 0 16 16">
                        <path fill="currentColor"
                            d="M12.25 0h-8.5A1.25 1.25 0 0 0 2.5 1.25v13.5A1.25 1.25 0 0 0 3.75 16h8.5a1.25 1.25 0 0 0 1.25-1.25V1.25A1.25 1.25 0 0 0 12.25 0zm0 14.75h-8.5V1.25h8.5z" />
                        <ellipse cx="8" cy="12.75" fill="currentColor" rx=".8" ry=".75" />
                    </svg>`,
            name: 'Mobile'
        }
    ],
    openMainCat(catIndex) {
        if (this.categoryList[catIndex].isOpen) {
            this.categoryList[catIndex].isOpen = false
        } else {
            this.categoryList.forEach(cat => cat.isOpen = false)
            this.categoryList[catIndex].isOpen = true
        }
    },
    openSubCat(catIndex, subCatIndex) {
        if (this.categoryList[catIndex].subCategories[subCatIndex].isOpen) {
            this.categoryList[catIndex].subCategories[subCatIndex].isOpen = false
        } else {
            this.categoryList.forEach(cat => {
                if (cat.subCategories) {
                    cat.subCategories.forEach(subCat => subCat.isOpen = false)
                }
            })
            this.categoryList[catIndex].subCategories[subCatIndex].isOpen = true
        }
    }
}

// Alpine Store
document.addEventListener('alpine:init', () => {
    Alpine.store('mobileMenu', {
        isOpen: false,
    })

    Alpine.store('category', {
        isCategory: false,
    })

    Alpine.store('search', {
        isSearch: false,
    })

    Alpine.store('cart', {
        isCart: false,
    })
})

// Price Range slider
function rangeslide(value) {
    document.getElementById('rangeValue').innerHTML = value;
}

// nice selector

let niceSelects = document.querySelectorAll(".nice-select")
for (nice of niceSelects) {
  NiceSelect.bind(nice);
}





