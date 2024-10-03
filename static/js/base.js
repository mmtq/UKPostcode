document.addEventListener("DOMContentLoaded", function() {
    // Polyfill for modulepreload support
    (function() {
        const r = document.createElement("link").relList;
        if (r && r.supports && r.supports("modulepreload")) return;

        for (const e of document.querySelectorAll('link[rel="modulepreload"]')) {
            l(e);
        }

        new MutationObserver(e => {
            for (const t of e) {
                if (t.type === "childList") {
                    for (const o of t.addedNodes) {
                        if (o.tagName === "LINK" && o.rel === "modulepreload") {
                            l(o);
                        }
                    }
                }
            }
        }).observe(document, {
            childList: true,
            subtree: true
        });

        function s(e) {
            const t = {};
            if (e.integrity) t.integrity = e.integrity;
            if (e.referrerPolicy) t.referrerPolicy = e.referrerPolicy;
            if (e.crossOrigin === "use-credentials") {
                t.credentials = "include";
            } else if (e.crossOrigin === "anonymous") {
                t.credentials = "omit";
            } else {
                t.credentials = "same-origin";
            }
            return t;
        }

        function l(e) {
            if (e.ep) return;
            e.ep = true;
            const t = s(e);
            fetch(e.href, t);
        }
    })();

    // Menu toggle logic
    var c = document.getElementById("toggleOpen");
    var d = document.getElementById("toggleClose");
    var n = document.getElementById("collapseMenu");

    function i() {
        if (n.style.display === "none" || n.style.display === "") {
            n.style.display = "block";
        } else {
            n.style.display = "none";
        }
    }

    // Check if the elements exist before adding event listeners
    if (c && d && n) {
        c.addEventListener("click", i);
        d.addEventListener("click", i);
    }

    // Add hover event listeners to elements with class 'relative'
    const relativeElement = document.querySelector(".relative");
    if (relativeElement) {
        relativeElement.addEventListener("mouseenter", function() {
            const menu = this.querySelector('div[role="menu"]');
            if (menu) menu.classList.remove("hidden");
        });

        relativeElement.addEventListener("mouseleave", function() {
            const menu = this.querySelector('div[role="menu"]');
            if (menu) menu.classList.add("hidden");
        });
    }
});
