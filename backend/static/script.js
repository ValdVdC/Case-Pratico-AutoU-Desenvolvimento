    document.getElementById('email-form').addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(e.target);
      const response = await fetch('/classify', { method: 'POST', body: formData });
      const data = await response.json();

      document.getElementById('categoria').textContent = data.categoria;
      document.getElementById('confianca').textContent = data.confianca;
      document.getElementById('resposta').textContent = data.resposta;
      document.getElementById('resultado').classList.remove('oculto');
    });