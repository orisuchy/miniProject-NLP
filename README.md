# miniProject-NLP

מיני פרוייקט בעיבוד שפה טבעית - דו״ח מסכם לניסוי
 בניית מסווג עבור מופעי המילה  ״אך״ בתנ״ך

מגישים: אורי סוכי, יעל חדד
מנחה: ד״ר מני אדלר

משימת עיבוד השפה העברית מאתגרת גם כאשר מדובר על עברית מודרנית, עבורה מאגרי הדאטה המתוייגים הולכים ומתרבים ומודלים רבים לבעיות שונות קיימים ואף ניתנים להתאמות לבעיות ספציפיות. 
עם זאת, משימה זו עבור הקורפוס התנ״כי מאתגרת אף יותר. סיבה אחת ומרכזית היא שהקורפוס הוא סגור ותיוגו משמעותו מתן פרשנות לתנ״ך, וזוהי משימה קשה בפני עצמה, ופירושים רבים ושונים קיימים ורבים מהם נתונים עד היום במחלוקת. 
משימתנו בפרויקט זה הינה בניית מסווג למציאת המשמעות של המילה "אך" בתנ"ך. את המשמעויות האפשריות לקחנו מתוך המילון והן:
אכן
רק
אבל
זה עתה

תהליך העבודה החל בתיוג כלל הדוגמאות מהפסוקים השונים באופן ידני, המשיך ביצירת וקטורי מאפיינים לכל פסוק וסוכם באימון מסווג על הדוגמאות ובדיקת איכותו בעזרת הכלי Weka. 

בנוסף למשימה הראשית, לאחר בחינת תוצאות הניסוי, החלטנו להוסיף שלב נוסף ומעניין, הבוחן את חשיבות גודל הדאטה להצלחת המסווג על ידי הקטנת מספר הדוגמאות בשני אופנים שונים - בחירה אקראית ובחירה המאזנת בין יחס הדוגמאות והתגים המתאימים. 

ראינו באופן מובהק כי אפילו בסדרי גודל קטנים, ככל שמספר הדוגמאות גדל, כך גדל הדיוק בסיווג ביחס לתיוג הידני. 

מפורטים שלבי התהליך הכוללים קישורים לקבצי דאטה וקוד באמצעותם בנינו את המסווג. 

קריאה מהנה. 
