// Функция для получения данных с API и вывода списка квартир
async function fetchApartments() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/v1/apartament/');
        if (!response.ok) {
            throw new Error('Failed to fetch apartments');
        }
        const data = await response.json();
        displayApartments(data);
    } catch (error) {
        console.error('Error fetching apartments:', error);
        alert('Failed to fetch apartments. Please try again later.');
    }
}

// Функция для вывода списка квартир на страницу в виде таблицы
function displayApartments(data) {
    const apartmentsTable = document.getElementById('apartmentsTable').getElementsByTagName('tbody')[0];
    
    // Очистка таблицы перед добавлением новых данных
    apartmentsTable.innerHTML = '';

    data.results.forEach(apartment => {
        const row = apartmentsTable.insertRow();
        const idCell = row.insertCell(0);
        const addressCell = row.insertCell(1);
        const status = row.insertCell(2);
        const floor = row.insertCell(3);
        const area = row.insertCell(4);
        const date = row.insertCell(5);
        const price = row.insertCell(6);
        const client = row.insertCell(7);
        const status_apartment = row.insertCell(8);

        idCell.textContent = apartment.number_apartament;
        addressCell.textContent = apartment.apartament_object;
        floor.textContent = apartment.floor;
        area.textContent = apartment.area;
        date.textContent = apartment.date;
        status.textContent = apartment.status;
        price.textContent = apartment.price;
        client.textContent = apartment.client;
        status_apartment.textContent = apartment.status_apartment;
    });
}

// Обработчик события для отправки данных формы на сервер
document.getElementById('apartmentForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    // Собираем данные из формы
    const formData = {
        number_apartament: document.getElementById('number_apartament').value,
        floor: document.getElementById('floor').value,
        area: document.getElementById('area').value,
        date: document.getElementById('date').value,
        status: document.getElementById('status').value,
        price: document.getElementById('price').value,
        client: document.getElementById('client').value,
        status_apartment: document.getElementById('status_apartment').value,
        apartament_object: document.getElementById('apartament_object').value
    };
    
    // Отправляем данные на сервер
    try {
        const response = await fetch('http://127.0.0.1:8000/api/v1/apartament/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            throw new Error('Failed to create apartment');
        }

        // Если запрос успешен, обновляем список квартир на странице
        fetchApartments();
    } catch (error) {
        console.error('Error creating apartment:', error);
        alert('Failed to create apartment. Please try again later.');
    }
});

// Вызываем функцию fetchApartments() при загрузке страницы
window.onload = fetchApartments;
