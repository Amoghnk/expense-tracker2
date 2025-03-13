// Helper function to make API calls
async function fetchData(url, method, data = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
        },
    };
    if (data) options.body = JSON.stringify(data);

    const response = await fetch(url, options);
    return response.json();
}

// Signup Form Submission
document.getElementById('signup-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const phone = document.getElementById('phone').value;

    try {
        const data = await fetchData('http://127.0.0.1:5000/signup', 'POST', { name, email, password, phone });
        alert(data.message);
        if (data.message === 'User created successfully') {
            window.location.href = 'login.html';
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during signup.');
    }
});

// Login Form Submission
document.getElementById('login-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const data = await fetchData('http://127.0.0.1:5000/login', 'POST', { email, password });
        alert(data.message);
        if (data.message === 'Login successful') {
            localStorage.setItem('user_id', data.user_id);
            window.location.href = 'index.html';
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during login.');
    }
});

// Load Expenses on Index Page
if (window.location.pathname.endsWith('index.html')) {
    const user_id = localStorage.getItem('user_id');
    if (!user_id) {
        window.location.href = 'login.html';
    }

    async function loadExpenses(category = '') {
        const url = `http://127.0.0.1:5000/get_expenses?user_id=${user_id}&category=${category}`;
        const expenses = await fetchData(url, 'GET');
        const tableBody = document.getElementById('expenses-table').getElementsByTagName('tbody')[0];
        tableBody.innerHTML = '';

        expenses.forEach(expense => {
            const row = tableBody.insertRow();
            row.insertCell(0).innerText = expense.amount;
            row.insertCell(1).innerText = expense.date;
            row.insertCell(2).innerText = expense.category;
            row.insertCell(3).innerText = expense.description;
        });
    }

    // Load expenses on page load
    loadExpenses();

    // Filter expenses by category
    document.getElementById('filter-category').addEventListener('change', (e) => {
        loadExpenses(e.target.value);
    });
}

// Add Expense Form Submission
document.getElementById('add-expense-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();

    const user_id = localStorage.getItem('user_id');
    const amount = document.getElementById('amount').value;
    const date = document.getElementById('date').value;
    const category = document.getElementById('category').value;
    const description = document.getElementById('description').value;

    try {
        const data = await fetchData('http://127.0.0.1:5000/add_expense', 'POST', { user_id, amount, date, category, description });
        alert(data.message);
        if (data.message === 'Expense added successfully') {
            window.location.href = 'index.html';
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while adding the expense.');
    }
});