const accordeon = () => {
    const chItems = document.querySelectorAll('.characteristics__item');

    const tabsClose = () => {
        chItems.forEach((el) => {
            el.querySelector('.characteristics__title').classList.remove('active');
            el.querySelector('.characteristics__description').classList.remove('open');
            el.querySelector('.characteristics__description').classList.remove('active');
            el.querySelector('.characteristics__description').style.height = '';
        });
    };
    tabsClose();
    chItems.forEach((item) => {
        const chButton = item.querySelector('.characteristics__title');
        const chContent = item.querySelector('.characteristics__description');
        chButton.addEventListener('click', (e) => {
            if (chContent.classList.contains('open')) {
                chContent.style.height = '';
            } else {
                tabsClose();
                chContent.style.height = chContent.scrollHeight + 'px';
            }
            chButton.classList.toggle('active');
            chContent.classList.toggle('open');
        });
    });
};

accordeon();
