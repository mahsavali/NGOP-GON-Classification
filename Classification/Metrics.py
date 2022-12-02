
# Define Metrics Evaluate
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, precision_score, confusion_matrix, roc_curve, recall_score
from sklearn.metrics import multilabel_confusion_matrix
import matplotlib.pyplot as plt
import itertools



def plot_confusion_matrix(cm, classes,
                        normalize=True,
                        title='Confusion matrix',
                        cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j],'.2f'),
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def specificity(y_true, y_pred):
    conf= multilabel_confusion_matrix(y_true, y_pred, labels=[0,1,2]).ravel()
    spe_0= conf[0]/(conf[0]+conf[1])
    spe_1= conf[4+0]/(conf[4+0]+conf[4+1])
    spe_2= conf[8+0]/(conf[8+0]+conf[8+1])

    specificity_score= (len(np.where(y_true==0)[0])*spe_0 + len(np.where(y_true==1)[0])*spe_1 + len(np.where(y_true==2)[0])*spe_2)/len(y_true)
    return specificity_score

def my_metrics(y_true, y_pred):

    accuracy=accuracy_score(y_true, y_pred)
    precision=precision_score(y_true, y_pred,average='weighted')
    f1Score=f1_score(y_true, y_pred, average='weighted') 
    recall=recall_score(y_true, y_pred, average='weighted') 
    specificity_score=specificity(y_true, y_pred)
    print("Accuracy  : {}".format(accuracy))
    print("f1Score  : {}".format(f1Score))
    print("Precision : {}".format(precision))
    print("recall : {}".format(recall))
    print("specificity : {}".format(specificity_score))

    cm=confusion_matrix(y_true, y_pred)
    print(cm)
    return accuracy, precision, f1Score, recall, specificity_score