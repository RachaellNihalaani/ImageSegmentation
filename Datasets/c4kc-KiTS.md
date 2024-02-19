Link - https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=61081171 

Region of Interest: Kidney and Kidney Tumor Segmentation

Data Description Manuscript - https://arxiv.org/pdf/1904.00445.pdf  
Github - https://github.com/neheller/kits19   [use this for better organised data]

When we download the .tcia files, we get a dataset that includes 3-phase CT scans (taken at different phases of contrast enhancement). Contrast enhancement in CT imaging involves the use of contrast agents to improve the visibility of internal structures. The three phases mentioned – noncontrast, arterial, and late – represent different timings in relation to the administration of the contrast agent. Here's what each phase means:

1. Noncontrast Phase:
* This phase involves taking CT scans without any contrast agent.
* It provides a baseline image of the anatomy and is useful for identifying calcifications, stones, and certain types of tumors.

2. Arterial Phase:
* This phase occurs shortly after the injection of the contrast agent, typically within 20-40 seconds.
* During this phase, the contrast agent is predominantly present in the arterial system.
* The arterial phase is particularly useful for evaluating vascular structures, such as arteries, and for detecting hypervascular lesions (lesions with a high density of blood vessels), which are more apparent in this phase.

3. Late (or Venous) Phase:
* This phase is captured a bit later, usually about 60-90 seconds after contrast injection.
* By this time, the contrast agent has moved from the arterial system into the venous system.
* The late phase is useful for evaluating organs and detecting lesions that are better visualized once the contrast agent has perfused through the vascular system into the tissues.

In the context of kidney tumor segmentation, these different phases can provide complementary information. For instance:
* The noncontrast phase can help in identifying the natural appearance of the kidney and any calcifications.
* The arterial phase can highlight highly vascularized tumors.
* The late phase can provide a more comprehensive view of the kidney structure and any abnormalities.

When analyzing such multi-phase CT data, it's important to consider the characteristics of each phase to accurately interpret the images and derive meaningful insights, especially in tasks like tumor segmentation or organ delineation.

------------------------------------------------------------------------------------------------------------------
When we clone data from github, and follow the Usage instructions, it will download 300 cases 
