// Copy the sample assignment language on Step 4.
document.querySelectorAll('.copybtn').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var box = btn.closest('details');
    var text = Array.from(box.querySelectorAll('li, p:not(.small)')).map(function (el) {
      if (el.tagName !== 'LI') return el.innerText;
      return (Array.from(el.parentNode.children).indexOf(el) + 1) + '. ' + el.innerText;
    }).join('\n\n');
    navigator.clipboard.writeText(text).then(function () {
      btn.textContent = 'Copied';
      setTimeout(function () { btn.textContent = 'Copy this language'; }, 2000);
    });
  });
});
