const scrollFunc = () => {
    const links = document.querySelectorAll('.header-menu__item a');
    const cardDetalis = document.querySelector('.card-details__link-characteristics');
    const newArray = [...links, cardDetalis];

    seamless.polyfill();

    newArray.forEach((el) => {
        el.addEventListener('click', (e) => {
            e.preventDefault();
            const id = el.getAttribute('href').substring(1);
            const section = document.getElementById(id);
            if (section) {
                seamless.elementScrollIntoView(section, {
                    behavior: 'smooth',
                    block: 'start',
                });
            }
        });
    });
};
scrollFunc();
