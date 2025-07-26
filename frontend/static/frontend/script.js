let usuarioId = null;
let usuarioNome = null;

async function loginUsuario() {

  //captura inicial dos ids dos campos no front
  const nome_usuario = document.getElementById('nome-usuario').value;
  const email = document.getElementById('login-email').value;
  const senha = document.getElementById('login-senha').value;
  const msg = document.getElementById('login-msg');

  //iniciando envio para o DB
  try {

      // solicitacao para ver se ja exite o usuario com nome, email e senha for true, envio a req...
      //isso la na view LoginOuCadastroUsuario que cria caso na exista no db
    const res = await fetch('/api/login/', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ nome_usuario, email, senha })  
      });

    const data = await res.json(); // conversao para json do obj vindo do DB

    if (!res.ok) {
      msg.textContent = data.error || 'Erro no login.';
      return;
    }

    //salva dados do usuaario logado
    usuarioId = data.usuario.usuario_id;    
    usuarioNome = data.usuario.nome_usuario; 

    msg.textContent = data.mensagem;

    document.getElementById('login-div').style.display = 'none';
    document.getElementById('calc-div').style.display = 'block';
    document.getElementById('user-nome').textContent = usuarioNome;

    loadHistory();
  } catch (error) {
    msg.textContent = "Erro ao conectar ao servidor.";
  }
}

const display = document.getElementById('display');
const historyList = document.getElementById('history');

function clearDisplay() {
  display.textContent = '0';
}

function deleteLast() {
  display.textContent = display.textContent.slice(0, -1) || '0';
}

function appendNumber(number) {
  if (display.textContent === '0') display.textContent = number;
  else display.textContent += number;
}

function appendOperator(operator) {
  const lastChar = display.textContent.slice(-1);
  if ("+-*/".includes(lastChar)) {
    display.textContent = display.textContent.slice(0, -1) + operator;
  } else {
    display.textContent += operator;
  }
}

async function calculate() {
  if (!usuarioId) return alert("Faça login primeiro!");

  const parametros = display.textContent;
  try {
    const response = await fetch(`/api/usuarios/${usuarioId}/operacoes/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ parametros })
    });

    if (!response.ok) {
        const err = await response.json();
        display.textContent = err.parametros || 'Erro'; //tratamento para capturar o tipo do erro para me localizar
        return;
    }

   
    loadHistory();
  } 
  
  catch (error) {
    display.textContent = 'Erro';
  }
}

async function loadHistory() {
  if (!usuarioId) return ;
  

  try {
    const response = await fetch(`/api/usuarios/${usuarioId}/operacoes/`);
    if(!response.ok) throw new Error("Erro na requaisicao") //caso n retorne 200
    
    const data = await response.json();

    if (data.length === 0) {
      historyList.innerHTML = '<li>Sem histórico ainda</li>'; 
      //tratamento para informar que de fato o banco nao entregou ou vouve algum error...
    }
    else
      historyList.innerHTML = '';

    
    data.forEach(op => {
      const li = document.createElement('li');
      li.textContent = `${op.parametros} = ${op.resultado}`;
      historyList.appendChild(li);
      
    });
  } 
  catch (error) {
    console.error('Erro ao carregar histórico:', error);
  }
}
