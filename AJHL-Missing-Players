
function HockeyTech_Stats_Update (){
updateCSVFromHockeyTech("https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=62&team=all&position=skaters&rookies=0&statsType=standard&rosterstatus=1&site_id=1&first=0&limit=1000&sort=points&league_id=1&lang=en&division=-1&conference=-1&key=f3ed30007ad2124e&client_code=bchl&league_id=1", "BCHL STATS");

updateCSVFromHockeyTech("https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=61&team=all&position=skaters&rookies=0&statsType=standard&rosterstatus=undefined&site_id=2&first=0&limit=1000&sort=points&league_id=3&lang=en&division=-1&conference=-1&key=2fb5c2e84bf3e4a8&client_code=sjhl&league_id=3", "SJHL STATS");

updateCSVFromHockeyTech("https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=42&team=all&position=skaters&rookies=0&statsType=standard&rosterstatus=1&site_id=2&first=0&limit=1000&sort=points&league_id=1&lang=en&division=-1&conference=-1&key=cbe60a1d91c44ade&client_code=ajhl&league_id=1", "AJHL STATS");

updateCSVFromHockeyTech("https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=51&team=all&position=skaters&rookies=0&statsType=standard&rosterstatus=undefined&site_id=2&first=0&limit=1000&sort=points&league_id=1&lang=en&division=-1&conference=-1&key=f894c324fe5fd8f0&client_code=mjhl&league_id=1", "MJHL STATS");

updateCSVFromHockeyTech("https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=38&team=all&position=skaters&rookies=0&statsType=standard&rosterstatus=undefined&site_id=2&first=0&limit=1000&sort=points&league_id=1&lang=en&division=-1&conference=-1&key=c1375ff55168bd71&client_code=nojhl&league_id=1", "NOJHL STATS");

updateCSVFromHockeyTech("https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=90&team=all&position=skaters&rookies=0&statsType=standard&rosterstatus=1&site_id=2&first=0&limit=1000&sort=points&league_id=1&lang=en&division=-1&conference=-1&key=34b10d4d34d7b59a&client_code=gojhl&league_id=1", "GOJHL STATS");

updateCSVFromHockeyTech("https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=37&team=all&position=skaters&rookies=0&statsType=standard&rosterstatus=undefined&site_id=2&first=0&limit=1000&sort=points&league_id=1&lang=en&division=-1&conference=-1&key=4a948e7faf5ee58d&client_code=mhl&league_id=1", "MHL STATS");

updateCSVFromHockeyTech("https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=85&team=all&position=skaters&rookies=0&statsType=standard&rosterstatus=undefined&site_id=0&first=0&limit=1000&sort=points&league_id=1&lang=en&division=-1&key=e828f89b243dc43f&client_code=ushl&league_id=1", "USHL STATS");

updateCSVFromHockeyTech("https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=26&team=all&position=skaters&rookies=0&statsType=standard&rosterstatus=undefined&site_id=2&first=0&limit=1000&sort=points&league_id=1&lang=en&division=-1&conference=-1&key=77a0bd73d9d363d3&client_code=ojhl&league_id=1", "OJHL STATS");

updateCSVFromHockeyTech("https://lscluster.hockeytech.com/feed/index.php?feed=statviewfeed&view=players&season=100&team=all&position=skaters&rookies=0&statsType=standard&rosterstatus=undefined&site_id=3&first=0&limit=1000&sort=points&league_id=1&lang=en&division=-1&conference=-1&key=b370f3e6c805baf3&client_code=cchl&league_id=1", "CCHL STATS");


}


function updateCSVFromHockeyTech(urlParameter, sheetName) {
  var url = urlParameter; // Replace with your CSV URL
  Logger.log(url);
  Logger.log(sheetName);
 var spreadSheet = SpreadsheetApp.getActiveSpreadsheet();
 var sheet = spreadSheet.getSheetByName(sheetName); // Get the sheet by name
  
  // Fetch JSON content
  var response = UrlFetchApp.fetch(url);
  var jsonData = response.getContentText();
  
  // Remove first and last parentheses if present
  if (jsonData.startsWith("(") && jsonData.endsWith(")")) {
    jsonData = jsonData.slice(1, -1); // Remove the first and last character (parentheses)
  }
  
  // Parse the cleaned JSON
  var parsedData = JSON.parse(jsonData);
  
  // Log the parsed JSON to see its structure
 console.log(parsedData);
  
  // Access the sections[0].data array if it exists
  if (parsedData[0].sections && parsedData[0].sections[0].data && Array.isArray(parsedData[0].sections[0].data)) {
    var data = parsedData[0].sections[0].data; // Extract data from sections[0].data
    
    // Clear the sheet before displaying new data
    sheet.clear();
    
    // Get headers from the first row of data (using Object.keys on 'row')
    var headers = Object.keys(data[0].row); // Extract headers from the first object inside 'row'
   // Logger.log(Object.keys(data[0].row));

  // Check if the sheet is empty or headers exist
  var existingHeaders = [];
  if (sheet.getLastRow() > 0 && sheet.getLastColumn() > 0) {
    existingHeaders = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
  }

  // If headers are missing, add them
  if (existingHeaders.length === 0 || existingHeaders.join() !== headers.join()) {
    sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  }
    
    // Map each row object to an array of values and insert them into the sheet
    var rows = data.map(function(item) {     
      return headers.map(function(header) {
      //   Logger.log(item.row[header]);
        return sanitizeData(item.row[header]); // Get the value corresponding to each header
      });
    });
    
    // Write the rows starting from row 2
    sheet.getRange(2, 1, rows.length, headers.length).setValues(rows);
    
    Logger.log("JSON data imported successfully");
  } else {
    Logger.log("No valid 'sections[0].data' found in the JSON response. Here's the structure of the response:");
  //  Logger.log(parsedData);
  }
}

function sanitizeData(value) {
  
  
  if (typeof value === "string") {
    // Replace unwanted characters like 'A' or any other you need to remove
    return value.replace(/'A'/g, "")
    .replace(/'C'/g, "")
    .replace(/(AP)/g, "")
    .replace(/'/g,"'")
    .replace(/'É'/g, "E")
    .replace(/'é'/g, "e")
    .replace(/'ô'/g, "O")
    .replace(/'/g, "'");
  }
  return value; // Return the value as is if it's not a string
}

