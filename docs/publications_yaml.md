# Publications

This page lists the research publications which have been carried out in the context of the HACC program, or papers that may be of interest to the HACC community.

## Contribute

If you would like to contribute to this page by adding a reference to your publication, please follow the [contribution guidelines](contributing.md)

## 2024

<table width="100%">
    <tr>
        <th width="200">Name</th>
        <th width="120">Author(s)</th>
        <th width="120">Institution</th>
        <th width="120">Link</th>
        <th width="500">Notes</th>
    </tr>

    {% for item in site.data.publications["2024"] %}
    <tr>
        <td>{{ item.title }}</td>
        <td>{{ item.author }}<em>et al.</em></td>
        <td>{{ item.institution }}</td>
        <td>
            <a href="{{ item.link }}">Paper</a>
            {% if item.github %}
                <br><a href="{{ item.github }}">GitHub</a></br>
            {% endif %}
        </td>
        <td>
            {{ item.abstract }}
        </td>
    </tr>
    {% endfor %}
</table>

---------------------------------------
<p class="copyright">Copyright&copy; 2022-2024 Advanced Micro Devices</p>
