function togglePasswordVisibility() {
    var passwordInput = document.getElementById('password');
    var button = passwordInput.nextElementSibling;
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        button.textContent = 'Hide';
    } else {
        passwordInput.type = 'password';
        button.textContent = 'Show';
    }
}
document.addEventListener('DOMContentLoaded', function() {
    const currentDate = new Date().toLocaleDateString('en-US', { 
        weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' 
    });
    document.getElementById('currentDate').textContent = currentDate;
});

document.addEventListener('DOMContentLoaded', function () {
    const currentDate = new Date();
    const currentMonth = currentDate.getMonth();
    const currentYear = currentDate.getFullYear();
    
    function loadCalendarDays(month, year) {
        const daysContainer = document.getElementById('dates');
        daysContainer.innerHTML = ''; // Clear previous cells
        let date = new Date(year, month, 1);
        while (date.getMonth() === month) {
            const dayCell = document.createElement('span');
            dayCell.innerText = date.getDate();
            if (date.getDate() === currentDate.getDate() && date.getMonth() === currentDate.getMonth()) {
                dayCell.classList.add('today');
            }
            daysContainer.appendChild(dayCell);
            date.setDate(date.getDate() + 1);
        }
    }

    document.querySelector('.prev-month').addEventListener('click', () => {
        loadCalendarDays(currentMonth - 1, currentYear);
    });

    document.querySelector('.next-month').addEventListener('click', () => {
        loadCalendarDays(currentMonth + 1, currentYear);
    });

    loadCalendarDays(currentMonth, currentYear); // Load current month
});

