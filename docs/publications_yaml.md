# Publications

This page lists the research publications which have been carried out in the context of the HACC program, or papers that may be of interest to the HACC community.

## Contribute

If you would like to contribute to this page by adding a reference to your publication, please follow the [contribution guidelines](contributing.md)

<!--
DO NOT MODIFY THIS FILE.

TO ADD YOUR PAPER, PLEASE EDIT THE YAML FILE IN docs/_data/publications/<year of publication>.yaml
-->


{% assign years = "2024,2023,2022,2016" | split: "," %}

Click in the year for easier search:

{% for year in years %}

- [{{ year }}](#{{ year }})

{% endfor %}

{% for year in years %}

## {{ year }}

<table width="100%">
    <tr>
        <th width="200">Name</th>
        <th width="120">Author(s)</th>
        <th width="120">Institution</th>
        <th width="120">Link</th>
        <th width="500">Notes</th>
    </tr>

    {% for item in site.data.publications[year] %}
    <tr>
        <td>
            {{ item.title }}
            {% if item.bestpaper %}
                <img src="./images/best_paper_award.png" alt="Best Paper" height="160">
            {% endif %}
        </td>
        <td>{{ item.author }}<em>et al.</em></td>
        <td>{{ item.institution }}</td>
        <td>
            <a href="{{ item.link }}">Paper</a>
            {% if item.github %}
                <br><a href="{{ item.github }}">GitHub</a>
            {% endif %}
        </td>
        <td>
            {{ item.abstract }}
        </td>
    </tr>
    {% endfor %}
</table>

{% endfor %}

---------------------------------------
<p class="copyright">Copyright&copy; 2022-2024 Advanced Micro Devices</p>
