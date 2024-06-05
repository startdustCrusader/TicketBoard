function deleteTicket(ticketId) {
  fetch("/delete-ticket", {
    method: "POST",
    body: JSON.stringify({ ticketId: ticketId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function updateTicket(ticketId, ticketName, ticketData) {
  console.log("Test - index json - update");
  fetch("/update-ticket", {
    method: "POST",
    body: JSON.stringify({
      ticketId: ticketId,
      ticketName: ticketName,
      ticketData: ticketData,
    }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
