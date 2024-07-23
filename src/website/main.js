fetch('data/data.json')
    .then(response => response.json())
    .then(data => {
        const tableContainer = document.getElementById('table-container');
        const table = document.createElement('table');

        // Define columns
        const columns = [
            { key: 'title', label: 'Title' },
            { key: 'employer', label: 'Employer' },
            { key: 'union', label: 'Union' },
            { key: 'arbitratorFirstName', label: 'Arbitrator First Name' },
            { key: 'arbitratorLastName', label: 'Arbitrator Last Name' },
            { key: 'awardIssueDate', label: 'Award Issue Date' },
            { key: 'natureOfGrievance', label: 'Nature of Grievance' },
            { key: 'industrialSectorType', label: 'Industrial Sector Type' },
            { key: 'labourAct', label: 'Labour Act' },
            { key: 'industry', label: 'Industry' },
            { key: 'sector', label: 'Sector' },
            { key: 'grievanceType', label: 'Grievance Type' }
        ];

        // Create table header
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        columns.forEach(column => {
            const th = document.createElement('th');
            th.textContent = column.label;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        // Create table body
        const tbody = document.createElement('tbody');
        data.forEach(item => {
            const row = document.createElement('tr');
            columns.forEach(column => {
                const td = document.createElement('td');
                if (column.key === 'title') {
                    const a = document.createElement('a');
                    a.href = item['url'];
                    a.textContent = item[column.key];
                    a.target = '_blank';
                    td.appendChild(a);
                } else {
                    td.textContent = item[column.key];
                }
                row.appendChild(td);
            });
            tbody.appendChild(row);
        });
        table.appendChild(tbody);

        tableContainer.appendChild(table);
    })
    .catch(error => console.error('Error fetching data:', error));
