{% extends 'main/layout.html' %}

{% block title %}
    Profile Page
{% endblock %}

{% block bodypage %}
<div class="profile-box">
  <form action="" method="get">
      <h1>Profile Information</h1>

      <div class="input-box">
          <input type="text" required enabled maxlength="30">
      </div>

      <div class="input-box">
          <input type="text" required enabled maxlength="30">
      </div>
      <div class="input-box">
          <input type="email" required enabled maxlength="30">
      </div>

      <div class="input-box">
          <input type="password" required enabled maxlength="20">
      </div>

      <center><button type="submit"><span>Save</span></button></center>
  </form>
</div>    
{% endblock %}
