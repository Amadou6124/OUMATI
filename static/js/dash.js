
        document.addEventListener('DOMContentLoaded', function() {
            // Initialiser tous les carrousels
            initGliders();
            
            function initGliders() {
                const gliders = document.querySelectorAll('.glider');
                
                gliders.forEach((glider, index) => {
                    new Glider(glider, {
                        slidesToShow: 2.5,
                        slidesToScroll: 1,
                        draggable: true,
                        dots: `.glider-dots`,
                        arrows: {
                            prev: `.glider-prev`,
                            next: `.glider-next`
                        },
                        responsive: [
                            {
                                breakpoint: 1200,
                                settings: {
                                    slidesToShow: 3.5,
                                    slidesToScroll: 2
                                }
                            },
                            {
                                breakpoint: 992,
                                settings: {
                                    slidesToShow: 2.5,
                                    slidesToScroll: 2
                                }
                            },
                            {
                                breakpoint: 768,
                                settings: {
                                    slidesToShow: 1.5,
                                    slidesToScroll: 1
                                }
                            }
                        ]
                    });
                });
            }
        });
   