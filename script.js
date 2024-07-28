
document.addEventListener('DOMContentLoaded', function () {
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


document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('appointment-form');
    const confirmation = document.getElementById('confirmation');
    const anotherAppointmentBtn = document.getElementById('another-appointment');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        form.classList.add('hidden');
        confirmation.classList.remove('hidden');
    });

    anotherAppointmentBtn.addEventListener('click', function () {
        form.reset();
        form.classList.remove('hidden');
        confirmation.classList.add('hidden');
    });
});

const supabaseUrl = 'https://cgwfbohodsudyhyuuxwa.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNnd2Zib2hvZHN1ZHloeXV1eHdhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjIwNjU1NzYsImV4cCI6MjAzNzY0MTU3Nn0.oLlmLnpGf09Edemcw8k8XanluU8wehFmTQ44HSg3dtM';
const client = supabase.createClient(supabaseUrl, supabaseKey);

document.addEventListener('DOMContentLoaded', async function () {
    // Get the user details from Supabase on authentication
    const { data: { user } } = await client.auth.getUser();

    console.log(user);

    // Function to update the welcome message with the user's full name
    function updateWelcomeMessage(userName) {
        const welcomeMessageElement = document.querySelector('.welcome-message h1');
        // Update the welcome message with the user's full name
        welcomeMessageElement.textContent = `Welcome, ${userName}`;
    }
    
    function updateprofilename(userName) {
        // Target the h1 element within the profile-info class inside profile-card
        const profileNameElement = document.querySelector('.profile-card .profile-info h1');
        // Update the profile name with the user's full name
        profileNameElement.textContent = userName;
    }
    
    // Check if the user object exists and has the full_name property
    if (user && user.user_metadata.first_name) {
        // updateWelcomeMessage("Ademola");
        updateWelcomeMessage(user.user_metadata.first_name);
        updateprofilename(`${user.user_metadata.first_name} ${user.user_metadata.last_name}`)
    } else {
        console.error('User details not found');
    }

});