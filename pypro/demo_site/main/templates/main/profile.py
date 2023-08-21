{% extends 'main/layout.html' %}

{% block title %}
    Profile Page
{% endblock %}

{% block bodypage %}
<div class="profile-box">
    <form method="get|post">
        {% csrf_token %}
        <table class="table inner1">
            <tbody>
                <tr>
                    <th colspan="2">
                        <h1>Profile Information</h1>
                    </th>
                </tr>
                <tr>
                    <td>Country:</td>
                    <td>{{}}</td>
                </tr>
                <tr>
                    <td>City:</td>
                    <td>{{}}</td>
                </tr>
                <tr>
                    <td>Age:</td>
                    <td>{{}}</td>
                </tr>
                <tr>
                    <td>Job title:</td>
                    <td>{{}}</td>
                </tr>
                <tr>
                    <td>Department:</td>
                    <td>{{}}</td>
                </tr>
                <tr>
                    <td>Extension number:</td>
                    <td>{{}}</td>
                </tr>
                <tr>
                    <td>Personal number:</td>
                    <td>{{}}</td>
                </tr>
                <tr>
                    <td>Outlook:</td>
                    <td>{{}}</td>
                </tr>
            </tbody>
        </table>
    </form>
    <div class="profile-inner2" style="border: thin solid grey;">
        <div class="inner2-head">
            <h2>
                {{}}
            </h2>
        </div>
        <div class="inner2-body">
            <div class="inner2-image">
                
            </div>
        </div>
        <div class="inner2-footer">
            <button class="inner2-btn">
                <a href="#" style="text-decoration: none;">Написать сообщение</a>
            </button>
            <button class="inner2-btn">
                <a href="#" style="text-decoration: none;">Сохранить</a>
            </button>
        </div>
    </div>
    </div>  
{% endblock %}
