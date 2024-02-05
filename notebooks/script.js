// Function to sort table data
function sortTable(table, column, asc = true) {
  const dirModifier = asc ? 1 : -1;
  const tBody = table.tBodies[0];
  const rows = Array.from(tBody.querySelectorAll('tr'));

  // Sort each row
  const sortedRows = rows.sort((a, b) => {
    const aColText = a.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim();
    const bColText = b.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim();

    return aColText > bColText ? (1 * dirModifier) : (-1 * dirModifier);
  });

  // Remove all existing TRs from the table
  while (tBody.firstChild) {
    tBody.removeChild(tBody.firstChild);
  }

  // Re-add the newly sorted rows
  tBody.append(...sortedRows);

  // Remember how the column is currently sorted
  table.querySelectorAll('th').forEach(th => th.classList.remove('th-sort-asc', 'th-sort-desc'));
  table.querySelector(`th:nth-child(${ column + 1 })`).classList.toggle('th-sort-asc', asc);
  table.querySelector(`th:nth-child(${ column + 1 })`).classList.toggle('th-sort-desc', !asc);
}

document.addEventListener('DOMContentLoaded', () => {
  // Query the table
  const table = document.querySelector('table');
  const headers = table.querySelectorAll('th');
  let currentIsAscending = true;

  // Listen for each click on table headers
  headers.forEach(header => {
    header.addEventListener('click', () => {
      const table = header.parentElement.parentElement.parentElement;
      const columnIndex = Array.from(header.parentElement.children).indexOf(header);
      const isAscending = header.classList.contains('th-sort-asc');
      sortTable(table, columnIndex, !isAscending);
    });
  });
});