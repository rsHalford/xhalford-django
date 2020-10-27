// function to set a given theme/color-scheme
function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}

// function to toggle between light and dark theme
function toggleTheme() {
    if (localStorage.getItem('theme') === 'theme-dark') {
        setTheme('theme-light');
    } else {
        setTheme('theme-dark');
    }
}

// Immediately invoked function to set the theme on initial load
(function () {
    if (localStorage.getItem('theme') === 'theme-dark') {
        setTheme('theme-dark');
        document.getElementById('slider').checked = false;
    } else {
        setTheme('theme-light');
        document.getElementById('slider').checked = true;
    }
})();


/*
const toggleColorMode = e => {
    if (e.currentTarget.classList.contains("light--hidden")) { //switch to light mode
        document.documentElement.setAttribute("color-mode", "light"); //set custom html attr
        localStorage.setItem("color-mode", "light"); //store user preference
        return;
    }
    
    document.documentElement.setAttribute("color-mode", "dark"); //set custom html attr
    localStorage.setItem("color-mode", "dark"); //store user preference
};

const toggleColorButtons = document.querySelectorAll(".color-mode__btn");

toggleColorButtons.forEach(btn => {
    btn.addEventListener("click", toggleColorMode);
});
*/
