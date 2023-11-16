<template>
    <div class="container">
        <div class="logreg-box">
            <div class="form-box login">
                <form action="#">
                    <h2>Iniciar Sesión</h2>
                    
                    <div class="input-box">
                        <input type="text" required>
                        <label>Nombre </label>
                    </div>

                    <div class="input-box">
                        <input type="text" required>
                        <label>Código</label>
                    </div>

                    <div class="input-box">
                        <input type="password" required>
                        <label>Contraseña</label>
                    </div>
                        <div class="remember-forgot">
                        <label><input type="checkbox">Recordar usuario</label>  
                        <a href="#">Olvidé la contraseña?</a>          
                    </div>

                    <button type="submit" class="btn">Iniciar sesión</button>
                </form>
            </div>
        </div>
    </div>
</template>


<script>
/* eslint-disable */ 
export default {
    name: 'Inicio',
}
</script>

<style>
body{
    overflow-y: hidden;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-size: cover;
  background-position: center;
}

.logreg-box .form-box.login{
    transition: transform .6s ease;
    transition-delay: 0s;
    border: 2px solid #0062b8;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
    padding: 15px
}

.logreg-box.active .form-box.login{
    transform: translateX(0);
    transition-delay: .7s;
}


.form-box h2 {
    font-size: 32px;
    text-align: center;
}

.form-box .input-box {
    position: relative;
    width: 340px;
    height: 50px;
    border-bottom: 2px solid #292727;
    margin: 30px 0;
}

.input-box input {
    width: 100%;
    height: 100%;
    background-color: transparent;
    border: none;
    outline: none;
    font-size: 16px;
    color: rgb(140 133 133);
    font-weight: 500;
    padding-right: 28px;
}

.input-box label {
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    font-size: 16px;
    font-weight: 500;
    pointer-events: none;
    transition: .5s ease;

}

.input-box input:focus~label,
.input-box input:valid~label {
    top: -5px;
}


.form-box .remember-forgot {
    font-size: 14.5px;
    font-weight: 500;
    margin: -15px 0 15px;
    display: flex;
    justify-content: space-between;
}

.remember-forgot label input {
    accent-color: rgb(41, 39, 39);
    margin-right: 3px;
}

.remember-forgot a {
    color:rgb(41, 39, 39);
    text-decoration: none;
}

.remember-forgot a:hover {
    text-decoration: underline;
}

.btn {
    width: 100%;
    height:  45px;
    background: #0062b8;
    border: none;
    outline: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    color: #e4e4e4;
    font-weight: 500;
    box-shadow: 0 0 10px rgba(0, 0, 0, .5);
}

</style>