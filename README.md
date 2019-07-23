## Pisces - Microsoft Azure Challenge 2019
With a greater focus on successful and sustainable fish farming operations, the need to regularly inspect fish health and behaviour, submerged infrastructure and the underwater environment is becoming increasingly urgent. Traditionally, specialist divers would do these but often at a considerable cost, while some underwater tasks are extremely dangerous. Hiring specialist divers also leaves a gap between what's going on underwater and the knowledge of farm employees working above water.

Our goal was to design an application encapsulating everything that fish-farm owners may need in everyday routine inspection and data analysis.ROVs are used in fish farms for regular inspections. However, it requires human labor as these inspections are done by steering the ROV and inspecting the nets and tanks manually. We harnessed Machine learning and the power of the cloud to automate those tasks with the intent to make the process faster, more efficient, and cost-effective. Pisces is a huge asset to any fish-farm that already utilizes ROVs in their routine inspections.

Pisces is an application that offers the following services to fish farm owners:

#### Fishing nets holes inspection.
Most fish farms have a fixed camera system to monitor what’s going on underwater, however, it’s too hard to get a full inspection of fishnet holes using these systems. Another option Fish farm owners resort to is to hire divers to do these inspections, but this can be quite expensive and inefficient. Pisces provides a service to inspect fishnet holes using the ROV’s cameras to get full access to areas which cannot be reached by divers. When a hole is found the application
sends a warning to the user so that it can be patched as soon as possible which helps in improving the fish farm production.


#### Fishing nets cleaning service.
The fish live in tanks all their lifetime in the fishing nets. These tanks are
exposed to sewage, dust and leftover food. As a result, waste start spreading out in the fishnets affecting the fish’s health. Pisces integrates a fishnet cleaning service that detects the cleanliness state of the fishnet to check whether it needs cleaning or not. By maneuvering the ROV in front of the fishnet and pressing the “Cleaning” button the current frame is analyzed to determine whether the fishnet needs cleaning or not. The label corresponding to the Fishnet needs cleaning field is then updated with the model’s prediction.


#### Water quality monitoring.
Pisces integrates an analytical model to predict water salinity level from sensors’
readings, ROV’s telemetry is analyzed through various data manipulation and
statistical functions. This helps generate a set of results that determine the water’s quality level which helps in knowing the surrounding environment’ s effect on the fish growth.

#### Pipes inspection:
Pipes are used to transport a variety of content every day to feed the fish and maintain constant temperature levels. It’s too hard to determine if the pipe has a crack or needs fixing as it is not convenient to have divers do these inspections manually. Pisces provides a service to determine if there are any cracks in the pipes or if they need fixing. This is done by positioning the ROV in front of the pipe to be inspected and pressing the “Pipes” button which consequently updates the label with the model’s prediction of whether the pipe needs to be changed or not.

We participated with this app in Microsoft Azure Machine Learning ROV Challenge 2019 in Tennessee, USA and were awarded the 1st place.

Make sure to check the Documentation here: https://drive.google.com/open?id=1zSFODKs4V49pMu21Px__RKyJmiVuDXze
