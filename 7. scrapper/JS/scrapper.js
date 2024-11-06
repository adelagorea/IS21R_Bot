const axios = require("axios");
const cheerio = require("cheerio");
const fs = require("fs");

async function fetchPage(url) {
  try {
    const { data } = await axios.get(url);
    return cheerio.load(data);
  } catch (error) {
    console.error(`Error fetching the URL: ${url}`, error);
    return null;
  }
}

async function scrapeAllPages() {
  const baseUrl = "https://999.md/ro/list/transport/cars?page=";
  let page = 1;
  let noAnnouncements = false;
  const today = new Date();
  const formattedDate = today.getFullYear() + "_" +
                      String(today.getMonth() + 1).padStart(2, '0') + "_" +
                      String(today.getDate()).padStart(2, '0');
  const resultsFile = `scrapped_${formattedDate}.json`;

  // Initialize the results file
  fs.writeFileSync(resultsFile, "[");

  while (!noAnnouncements) {
    const url = `${baseUrl}${page}`;
    const $ = await fetchPage(url);

    if (!$) {
      console.error(`Failed to load page ${page}`);
      break;
    }

    const announcements = $(".ads-list-photo.large-photo .ads-list-photo-item");

    if (announcements.length === 0) {
      noAnnouncements = true;
      console.log(`No announcements found on page ${page}. Stopping.`);
      break;
    }

    let pageResults = [];

    announcements.each((index, element) => {
      const $element = $(element);
      const classes = $element.attr("class");
      if (
        classes.includes("js-booster-inline") ||
        classes.includes("is-adsense")
      ) {
        return;
      }

      const titlu_element = $element.find(".ads-list-photo-item-title a");
      const pret_element = $element.find(".ads-list-photo-item-price-wrapper");

      const titlu = titlu_element.text().trim();
      const pret = pret_element.text().trim().replace(" ", " ");
      const href = titlu_element.attr("href");
      const id = href ? href.split("/").pop() : null;
      const img_element = $element.find(".ads-list-photo-item-thumb img");
      const img_url = img_element?.attr("src");

      if (!titlu || !id) {
        return;
      }

      pageResults.push({
        id: id,
        title: titlu,
        price: pret,
        image: img_url,
      });
    });

    if (pageResults.length > 0) {
      const data = JSON.stringify(pageResults, null, 4).slice(1, -1); // Remove surrounding brackets
      fs.appendFileSync(resultsFile, (page > 1 ? "," : "") + data);
    }

    console.log(`Page ${page} processed.`);
    page++;
  }

  // Finalize the results file
  fs.appendFileSync(resultsFile, "]");
  console.log("Results have been saved to results.json");
}

// Start scraping
scrapeAllPages();
